#!/usr/bin/env python3
"""B1 pre-publish content check for CFM Corner.

Reads committed bytes from a git tree (never the working tree), so it checks exactly what a
push would publish. Refuses on:

  BIBLEHUB   any "biblehub" in a checked file: parsed links, popup lists, visible text, and
             a raw-byte backstop for shapes the parser does not model (scripts, comments)
  HOST       a popup/lexicon link outside the shared list's "popup" hosts, or a URL in
             shared popup data outside "popup" (links) or "media" (audio/images)
  SECTIONS   resources.html lacks one of the three video sections
  VISIBLE    a web address appears in text a reader can see

r7 (2026-11-28), Kymber's answer "Only today's reference": the exception allows exactly ONE Bible Hub reference on that page,
the URL https://biblehub.com/ that is there today, at most once. An added or different Bible Hub link on the
page is refused; wording around the link may change. Supersedes r6's whole-page scope.
r6 (2026-11-28), Kymber's answer "Allow that one page": ONE named exception. content/resources/digital-tools.md,
matched by its exact repo path, may keep its Bible Hub reference; every other page is still refused.
It lifts GUIDE-BH findings on that path only, and every finding it lifts is PRINTED, never silent.
r5 (2026-11-27): an approved host matches with and without "www." (no other subdomain).
r4 (2026-11-27), after Kymber's look: popup and lexicon
destinations in HTML are judged by the shared reader's scan_popup_hosts (the ONE destination reader), loaded from
a fixed path and pinned by sha, with the policy built from the ONE host list; B1 keeps its own
Bible Hub count (parsed + raw backstop), visible-URL, section and shared-data checks; and
content/** (field guides, articles, archive) gets the Bible-Hub-only backstop she added.
r3 (2026-11-27), after review: a week-numbered data file adds its week AND is
scanned as a shared file.
r2 (2026-11-27), after review: raw-byte Bible Hub backstop (R1); a push that
changes shared data/layout files scans those files, and a week-numbered data file adds its
week (R2); a zero-week result says why and lists the changed paths (R3). Also: URLs in any
data-popup-* attribute are judged as popup links; the host list is ONE shared file
(--hosts), read by every reader, and a missing or unreadable list cannot vouch.

Exit codes (same as the firewall checkers): 0 pass · 1 refuse · 2 cannot vouch.
"""
import argparse, hashlib, importlib.util, json, re, subprocess, sys
from html.parser import HTMLParser
from urllib.parse import urlsplit

SECTIONS = [("Video Commentary", r"VIDEO COMMENTARY"),
            ("Women's Perspectives", r"WOMEN(?:'|’|&#8217;|&rsquo;)S PERSPECTIVES"),
            ("Family & Children's Resources", r"FAMILY (?:&|&amp;) CHILDREN(?:'|’|&#8217;|&rsquo;)S RESOURCES")]
URL_RE = re.compile(r"(?:https?://|www\.)[^\s<>\"')\]]+", re.I)
RAW_RE = re.compile(r"biblehub", re.I)
MEDIA_KEYS = {"audio", "image", "img", "src", "thumbnail", "thumb", "icon"}
SHARED_PREFIXES = ("static/data/", "themes/", "layouts/", "assets/", "static/js/", "static/css/")
# Her named exceptions: exact repo path -> (what the exception is, the ONE exact URL allowed, at most once).
# GUIDE-BH (Bible Hub on a content page) only.
GUIDE_BH_EXCEPTIONS = {
    "content/resources/digital-tools.md": (
        "the Digital Tools page keeps its one Bible Hub reference (Kymber, 2026-11-28)",
        "https://biblehub.com/"),
}


def split_exception(g, text, gf):
    """r7: lift at most ONE Bible Hub occurrence on an excepted page, and only one that lies inside
    an exact match of the allowed URL. Every other occurrence on the page stays a finding."""
    dec, url = GUIDE_BH_EXCEPTIONS[g]
    spans = [m.span() for m in URL_RE.finditer(text) if m.group() == url]
    pos = next((m.start() for m in RAW_RE.finditer(text) if any(a <= m.start() < b for a, b in spans)), None)
    rest, allowed = list(gf), []
    if pos is not None:
        ln = text.count("\n", 0, pos) + 1
        for i, f in enumerate(rest):
            if f[2] == ln:
                allowed = [(dec,) + rest.pop(i)[1:]]
                break
    note = f"biblehub — not the one reference her exception allows ({url}, once)"
    return [f[:4] + (note,) for f in rest], allowed
POPUP_ATTRS = ("data-lexicon", "data-strongs", "data-popup-links", "data-popup-kind", "data-popup-text")


class CannotVouch(Exception):
    pass


def www_twin(h):
    return h[4:] if h.startswith("www.") else "www." + h


def load_hosts(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
        hosts = {k: {h.lower() for h in d[k]} for k in ("refused", "popup", "media")}
        hosts["pending"] = {h.lower() for h in d.get("pending_her_choice", {})}
        hosts["popup"] -= hosts["pending"]          # a pending host is not approved
        # r5: she approved SITES, so each approved host matches
        # with and without a leading "www." — that twin only, no other subdomain.
        for k in ("popup", "media"):
            hosts[k] = hosts[k] | {www_twin(h) for h in hosts[k]}
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as e:
        raise CannotVouch(f"host list {path!r} missing or unreadable ({type(e).__name__})")
    if "biblehub.com" not in hosts["refused"] or not hosts["popup"]:
        raise CannotVouch("host list must refuse biblehub.com and name at least one popup host")
    return hosts


def load_ash_reader(path, expect_sha16):
    """The shared reader's scan_popup_hosts, the ONE destination reader.
    Loaded from a fixed path and pinned by sha: a missing or changed reader cannot vouch."""
    try:
        b = open(path, "rb").read()
    except OSError as e:
        raise CannotVouch(f"shared reader {path!r} missing ({type(e).__name__})")
    got = hashlib.sha256(b).hexdigest()[:16]
    if got != expect_sha16:
        raise CannotVouch(f"shared reader {path!r} is sha {got}, expected {expect_sha16}")
    spec = importlib.util.spec_from_file_location("cfm_shared_popup_reader", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name in ("scan_popup_hosts", "PopupHostPolicy"):
        if not hasattr(mod, name):
            raise CannotVouch(f"shared reader has no {name}")
    return mod


def host_of(u):
    if u.lower().startswith("www."):
        u = "https://" + u
    if u.startswith("//"):
        u = "https:" + u
    try:
        return (urlsplit(u).hostname or "").lower()
    except ValueError:
        raise CannotVouch(f"unparseable URL {u[:80]!r}")


def refused(h, hosts):
    return any(h == r or h.endswith("." + r) for r in hosts["refused"])


class Page(HTMLParser):
    """Every followable URL with its kind, and every URL in visible text."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.visible, self.skip = [], [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        a = dict(attrs)
        line = self.getpos()[0]
        popup = tag == "a" and any(k in a for k in POPUP_ATTRS)
        for k, v in attrs:
            if v is None:
                continue
            if k == "data-popup-links":
                try:
                    items = json.loads(v)
                except ValueError:
                    raise CannotVouch(f"line {line}: data-popup-links is not JSON")
                for it in items:
                    self.links.append((line, "popup-list", it.get("href", "")))
            elif k in ("href", "src"):
                self.links.append((line, "popup-anchor" if (popup and k == "href") else k, v))
            elif k not in ("title", "alt"):
                for m in URL_RE.finditer(v):
                    kind = "popup-attr:" + k if k.startswith("data-popup") or k == "data-lexicon" else "attr:" + k
                    self.links.append((line, kind, m.group(0)))

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            for m in URL_RE.finditer(d):
                self.visible.append((self.getpos()[0], m.group(0)))


def raw_backstop(name, text, found):
    """R1: every "biblehub" in the raw bytes is a finding; parsed findings keep their detail,
    and any occurrence the parser did not account for is added with its line."""
    raw = [text.count("\n", 0, m.start()) + 1 for m in RAW_RE.finditer(text)]
    extra = len(raw) - len(found)
    if extra <= 0:
        return []
    per_line = {}
    for ln in raw:
        per_line[ln] = per_line.get(ln, 0) + 1
    for f in found:
        per_line[f[2]] = per_line.get(f[2], 0) - 1
    lines = [ln for ln, n in sorted(per_line.items()) for _ in range(max(n, 0))][:extra]
    lines += [0] * (extra - len(lines))
    return [("BIBLEHUB", name, ln, "raw-bytes", "biblehub (not in a parsed link)") for ln in lines]


def check_html(name, text, hosts, ash):
    p = Page()
    p.feed(text)
    p.close()
    out = []
    for line, kind, u in p.links:
        if not u.lower().startswith(("http://", "https://", "//", "www.")):
            continue  # relative, anchor, mailto, javascript
        if refused(host_of(u), hosts):
            out.append(("BIBLEHUB", name, line, kind, u))
    # Popup, lexicon and LXX destinations: the shared reader. Its Bible Hub findings are
    # already counted above (parsed + raw backstop), so only its other findings are added.
    policy = ash.PopupHostPolicy(frozenset(hosts["popup"]), frozenset(hosts["refused"]))
    report = ash.scan_popup_hosts(text.encode("utf-8"), policy=policy)
    for f in report["findings"]:
        h = (f.get("host") or "")
        if h and refused(h.lower(), hosts):
            continue
        out.append(("HOST", name, f.get("line") or 0, f"{f.get('rule')}:{f.get('attribute')}",
                    f"{h or '(no host)'} — {f.get('detail')}"))
    for line, u in p.visible:
        if refused(host_of(u), hosts):
            out.append(("BIBLEHUB", name, line, "visible-text", u))
        out.append(("VISIBLE", name, line, "visible-text", u))
    out += raw_backstop(name, text, [f for f in out if f[0] == "BIBLEHUB"])
    return out


def check_sections(name, text):
    out = []
    for label, pat in SECTIONS:
        # the heading as a reader sees it: a dropdown <span> or an <h2>, never an HTML comment
        if not re.search(r"(?:<span>|<h2[^>]*>)\s*(?:&#9654;|▶)?\s*" + pat, text, re.I):
            out.append(("SECTIONS", name, 0, "missing", label))
    return out


def check_shared(name, text, hosts):
    """R2(b): a changed shared data/layout file. Backstop everywhere; for JSON, every URL
    value is judged — media keys against "media", every other key against "popup"."""
    out = []
    if name.endswith(".json"):
        try:
            data = json.loads(text)
        except ValueError:
            raise CannotVouch(f"{name} is not valid JSON")
        def walk(o, key):
            if isinstance(o, dict):
                for k, v in o.items():
                    walk(v, k)
            elif isinstance(o, list):
                for v in o:
                    walk(v, key)
            elif isinstance(o, str):
                for m in URL_RE.finditer(o):
                    u = m.group(0)
                    h = host_of(u)
                    tier = "media" if (key or "").lower() in MEDIA_KEYS else "popup"
                    if refused(h, hosts):
                        out.append(("BIBLEHUB", name, 0, f"json:{key}", u))
                    elif h not in hosts[tier]:
                        out.append(("HOST", name, 0, f"json:{key}", u))
        walk(data, None)
    out += raw_backstop(name, text, [f for f in out if f[0] == "BIBLEHUB"])
    return out


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode:
        raise CannotVouch(f"git {' '.join(args[:2])} failed: {r.stderr.strip()[:200]}")
    return r.stdout


def plan(repo, tree, base):
    """-> (weeks {weekNN: [files]}, shared [paths], changed [paths] or None, why)"""
    names = git(repo, "ls-tree", "-r", "--name-only", tree, "static/content/").split()
    by_week = {}
    for n in names:
        m = re.match(r"static/content/(week\d+)/[^/]+\.html$", n)
        if m:
            by_week.setdefault(m.group(1), []).append(n)
    if not by_week:
        raise CannotVouch("no static/content/weekNN/*.html in the pushed tree")
    if not base:
        guides = [n for n in git(repo, "ls-tree", "-r", "--name-only", tree, "content/").split()
                  if n.endswith((".md", ".html"))]
        return by_week, [], None, "every week (no base given)", guides
    changed = git(repo, "diff", "--name-only", "--no-renames", base, tree).split("\n")
    changed = [c for c in changed if c]
    touched, shared, guides = set(), [], []
    for c in changed:
        # her 'Yes, add it': field guides, articles and archive pages get the Bible-Hub-only check
        if c.startswith("content/") and c.endswith((".md", ".html")):
            guides.append(c)
        m = (re.match(r"static/content/(week\d+)/", c) or re.match(r"content/weeks/0*(\d+)\.md$", c)
             or re.match(r"static/data/.*?week0*(\d+)\b[^/]*$", c))
        if m:
            g = m.group(1)
            touched.add(g if g.startswith("week") else f"week{int(g):02d}")
        # r3: a week-numbered data file adds its week AND is scanned itself —
        # it feeds that week's popups when the page is served.
        if c.startswith(SHARED_PREFIXES):
            shared.append(c)
    weeks = {w: f for w, f in by_week.items() if w in touched}
    return weeks, shared, changed, "weeks this push changes", guides


def run(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo")
    ap.add_argument("--tree", help="commit/tree to check (the pushed sha)")
    ap.add_argument("--base", help="remote sha: check only what changed since it")
    ap.add_argument("--week", action="append", help="limit to weekNN (repeatable)")
    ap.add_argument("--files", nargs="+", help="loose files (controls); resources.html gets the section check")
    ap.add_argument("--hosts", required=True, help="the ONE shared approved-host list (JSON)")
    ap.add_argument("--ash-reader", required=True, help="path to the shared reader holding scan_popup_hosts")
    ap.add_argument("--ash-sha", required=True, help="first 16 hex of the shared reader's sha256")
    a = ap.parse_args(argv)
    try:
        hosts = load_hosts(a.hosts)
        findings, checked, shared_done, guides_done, changed, why = [], [], [], [], None, "files named"
        allowed = []   # findings lifted by a named exception: printed, never counted
        ash = load_ash_reader(a.ash_reader, a.ash_sha)
        if a.files:
            for f in a.files:
                t = open(f, encoding="utf-8").read()
                if f.endswith(".md"):
                    findings += [("GUIDE-BH",) + x[1:] for x in raw_backstop(f, t, [])]   # field-guide page: Bible-Hub-only
                elif f.endswith(".json") or not f.endswith((".html", ".htm")):
                    findings += check_shared(f, t, hosts)
                else:
                    findings += check_html(f, t, hosts, ash)
                    if f.endswith("resources.html"):
                        findings += check_sections(f, t)
                checked.append(f)
        else:
            if not (a.repo and a.tree):
                raise CannotVouch("need --repo and --tree, or --files")
            weeks, shared, changed, why, guides = plan(a.repo, a.tree, a.base)
            if a.week:
                weeks = {w: f for w, f in weeks.items() if w in a.week}
                why = "weeks named with --week"
                guides = []   # a named-week run checks those weeks only
            for w in sorted(weeks):
                files = weeks[w]
                if f"static/content/{w}/resources.html" not in files:
                    findings.append(("SECTIONS", f"static/content/{w}/resources.html", 0, "missing", "no resources.html"))
                for f in files:
                    t = git(a.repo, "show", f"{a.tree}:{f}")
                    findings += check_html(f, t, hosts, ash)
                    if f.endswith("/resources.html"):
                        findings += check_sections(f, t)
                checked.append(w)
            for s in shared:
                exists = subprocess.run(["git", "-C", a.repo, "cat-file", "-e", f"{a.tree}:{s}"],
                                        capture_output=True, stdin=subprocess.DEVNULL).returncode == 0
                if exists:  # a deleted file publishes nothing
                    findings += check_shared(s, git(a.repo, "show", f"{a.tree}:{s}"), hosts)
                    shared_done.append(s)
            for g in guides:
                exists = subprocess.run(["git", "-C", a.repo, "cat-file", "-e", f"{a.tree}:{g}"],
                                        capture_output=True, stdin=subprocess.DEVNULL).returncode == 0
                if exists:
                    gf = [("GUIDE-BH",) + f[1:] for f in raw_backstop(g, git(a.repo, "show", f"{a.tree}:{g}"), [])]
                    if g in GUIDE_BH_EXCEPTIONS:
                        refused, ok = split_exception(g, git(a.repo, "show", f"{a.tree}:{g}"), gf)
                        findings += refused
                        allowed += ok
                    else:
                        findings += gf
                    guides_done.append(g)
    except CannotVouch as e:
        print(f"CONTENT-CHECK CANNOT VOUCH — {e}", file=sys.stderr)
        return 2
    except Exception as e:  # fail closed on anything unexpected
        print(f"CONTENT-CHECK CANNOT VOUCH — {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    counts = {}
    for f in findings:
        counts[f[0]] = counts.get(f[0], 0) + 1
    label = ", ".join(checked) if len(checked) < 12 else f"{len(checked)} {'files' if a.files else 'weeks'}"
    print(f"CONTENT-CHECK checked {len(checked)} ({why}): {label}")
    if shared_done:
        print(f"  also scanned {len(shared_done)} shared data/layout file(s): {', '.join(shared_done[:10])}")
    if guides_done:
        print(f"  also scanned {len(guides_done)} field-guide/article page(s) for Bible Hub only"
              + (f": {', '.join(guides_done[:10])}" if len(guides_done) <= 10 else ""))
    if not checked:
        what = ("no popup data and no layout" if not (shared_done or guides_done)
                else "only the shared or field-guide files above")
        print(f"  checked 0 weeks: this push changes no weekly page; it changes {what}. Changed paths"
              + (f" ({len(changed)}):" if changed else ": none"))
        for c in (changed or [])[:20]:
            print(f"    {c}")
        if changed and len(changed) > 20:
            print(f"    … and {len(changed) - 20} more")
    for k in ("BIBLEHUB", "HOST", "SECTIONS", "VISIBLE", "GUIDE-BH"):
        print(f"  {k:9s} {counts.get(k, 0)}")
    for kind, name, line, how, what in findings:
        print(f"  {kind:9s} {name}:{line} [{how}] {what[:120]}")
    for dec, name, line, how, what in allowed:
        print(f"  ALLOWED   {name}:{line} [{how}] {what[:80]} (her named exception: {dec})")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(run())
