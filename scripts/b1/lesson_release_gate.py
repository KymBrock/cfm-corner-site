#!/usr/bin/env python3
"""Run CFM's existing evidence checks at a named transition.

This is deliberately an orchestrator, not a replacement checklist. It records
whether the prerequisite checks actually ran and passed for one exact lesson
root. It never writes lesson prose, creates review receipts, regenerates pages,
or grants publication permission.

Stages:
  prepare  -- lesson-start reading record plus preparation evidence
  rendered -- generated HTML scripture-target contract
  handoff  -- current handoff evidence plus the rendered contract

Examples:
  python3 verification/lesson_release_gate.py --week 40 --week-dir /path/to/Week_40... --stage prepare
  python3 verification/lesson_release_gate.py --week 40 --week-dir /path/to/Week_40... --stage rendered --rendered-dir /path/to/static/content/week40

A passed stage means only its named evidence is current. Human reader review,
Kymber's acceptance, and publication authorization remain separate decisions.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
MAX_INPUT_FILE = 8 * 1024 * 1024
MAX_INPUT_READS = 32 * 1024 * 1024


POPUP_HOST = "www.blueletterbible.org"
# Default list, used only when no policy is passed. The B1 check always passes its policy.
POPUP_HOST_LIST = Path(__file__).resolve().parent / "approved_hosts.json"
HOSTNAME = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")
LXX_LABEL = re.compile(
    r"^(?:(?:BLB\s+)?Septuagint\b|Swete(?:'s)?\b|LXX(?:\s*$|\s*[,:\u2014]|\s+(?:verse|source|text|passage)\b))",
    re.I,
)
LXX_CONTEXT = re.compile(r"\b(?:LXX|Septuagint|Swete)\b", re.I)
POPUP_URL_ATTRIBUTE = re.compile(r"data-(?:popup|lexicon|lxx|ref|scripture)(?:-[a-z0-9]+)*-(?:href|url|link)$")
JSON_URL_KEY = re.compile(r"(?:^|[-_])(?:href|url|link)$", re.I)
URL_START = re.compile(r"^\s*(?:[a-z][a-z0-9+.-]*:|//)", re.I)


class PopupHostPolicyError(ValueError):
    """The shared list cannot safely be used to measure destinations."""


class PopupHostPolicy(NamedTuple):
    popup: frozenset[str]
    refused: frozenset[str]

    def refuses(self, host: str) -> bool:
        host = host.rstrip(".")
        return any(host == domain or host.endswith("." + domain) for domain in self.refused)


def load_popup_host_policy() -> PopupHostPolicy:
    try:
        data = json.loads(POPUP_HOST_LIST.read_bytes())
        refused = data["refused"]
        popup = data["popup"]
        pending = data["pending_her_choice"]
        if not isinstance(refused, list) or not isinstance(popup, list) or not isinstance(pending, dict):
            raise ValueError("Expected refused and popup arrays and a pending_her_choice object")
        if any(not isinstance(host, str) or not HOSTNAME.fullmatch(host)
               for host in (*refused, *popup, *pending)):
            raise ValueError("Host lists must contain exact lowercase hostnames")
        policy = PopupHostPolicy(frozenset(popup).difference(pending), frozenset(refused))
        if "biblehub.com" not in policy.refused or any(policy.refuses(host) for host in popup):
            raise ValueError("The list must refuse biblehub.com and omit refused domains from popups")
        if POPUP_HOST not in policy.popup:
            raise ValueError(f"The list must allow the lexicon and LXX source host {POPUP_HOST}")
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, RecursionError) as exc:
        raise PopupHostPolicyError(f"Invalid popup host list {POPUP_HOST_LIST}: {exc}") from exc
    return policy


class _PopupHosts(HTMLParser):
    """Inspect all anchor destinations and the extra links shown inside popups."""

    def __init__(self, policy: PopupHostPolicy, *, embedded_at: int | None = None) -> None:
        super().__init__(convert_charrefs=True)
        self.policy = policy
        self.measured = 0
        self.popup_links = 0
        self.findings: list[dict] = []
        self.anchor = None
        self.row_lxx: bool | None = None
        self.row_sources = []
        self.embedded_at = embedded_at

    def _finding(self, line, attribute, host, detail, *, rule="POPUP-HOST-NOT-APPROVED"):
        self.findings.append({
            "rule": rule, "line": line, "attribute": attribute,
            "host": host, "detail": detail,
        })

    def _destination(self, href, label, line, attribute, *, lexicon=False, popup=False, lxx=False):
        self.measured += 1
        self.popup_links += int(lexicon or popup)
        host, scheme, authority, path = None, "", "", ""
        href = (href or "").strip()
        try:
            target = urlsplit(href)
            host, scheme, authority, path = target.hostname, target.scheme, target.netloc.lower(), target.path.lower()
        except ValueError:
            pass
        if host and self.policy.refuses(host):
            detail = ("Bible Hub is not an approved Reader destination"
                      if host.rstrip(".").split(".")[-2:] == ["biblehub", "com"]
                      else "Destination is refused by the shared popup host list")
            self._finding(line, attribute, host, detail)
            return
        https = scheme == "https" and bool(authority)
        lxx = lxx or path.startswith(("/lxx/", "/sepd/")) or bool(LXX_LABEL.search(label))
        if lexicon:
            if not (https and authority == POPUP_HOST):
                self._finding(line, attribute, host, f"Lexicon popups require https://{POPUP_HOST} (LEXICON-POPUP-SPEC.md)")
        elif lxx:
            if not (https and authority == POPUP_HOST and path.startswith("/lxx/")):
                self._finding(line, attribute, host, f"LXX source links require https://{POPUP_HOST}/lxx/")
        elif popup:
            # Local in-page and site links have no outbound host.
            local = href.startswith(("#", "/")) and not href.startswith("//") and not authority and "\\" not in href
            if not (local or (https and authority in self.policy.popup)):
                self._finding(line, attribute, host, "Popup source link uses an unapproved HTTPS authority")

    def _json_links(self, raw, line):
        attribute = "data-popup-links"
        try:
            rows = json.loads(raw or "")
        except (ValueError, RecursionError):
            rows = None
        if not isinstance(rows, list):
            self._finding(line, attribute, None, "Popup links must be a JSON array", rule="POPUP-LINK-DATA-INVALID")
            return
        pending = [(row, "") for row in reversed(rows)]
        while pending:
            item, label = pending.pop()
            if isinstance(item, dict):
                item_label = item.get("label")
                label = " ".join(item_label.split()) if isinstance(item_label, str) else label
                for key, value in item.items():
                    if key == "label":
                        continue
                    if JSON_URL_KEY.search(key):
                        if isinstance(value, str) and value.strip():
                            self._destination(value, label, line, attribute, popup=True,
                                              lxx=key.lower().startswith("lxx"))
                        else:
                            self._finding(line, attribute, None, "Popup URL must be a string", rule="POPUP-LINK-DATA-INVALID")
                    elif isinstance(value, (dict, list)) or (isinstance(value, str) and URL_START.match(value)):
                        pending.append((value, label))
            elif isinstance(item, list):
                pending.extend((value, label) for value in reversed(item))
            elif isinstance(item, str) and URL_START.match(item):
                self._destination(item, label, line, attribute, popup=True)

    def _finish_anchor(self):
        if self.anchor is None:
            return
        values, line, chunks = self.anchor
        self.anchor = None
        label = " ".join("".join(chunks).split())
        title = " ".join((values.get("title") or "").split())
        attribute = "data-popup-text" if self.embedded_at is not None else "href"
        source_popup = values.get("data-popup-kind") == "source"
        lexicon = "data-lexicon" in values and not source_popup
        # data-ref alone identifies a scripture citation. Its visible href is
        # not an extra source shown in the popup, whose links are scanned separately.
        popup = self.embedded_at is not None or any(k in values for k in ("data-popup-kind", "data-popup-links", "data-ref"))
        lxx = bool(LXX_LABEL.search(title))
        args = (values.get("href"), label, line, attribute)
        if label.casefold() in {"source passage", "source text"} and self.row_lxx is not None and not lexicon:
            self.row_sources.append((args, popup, lxx))
        else:
            self._destination(*args, lexicon=lexicon, popup=popup, lxx=lxx)

    def _finish_row(self):
        self._finish_anchor()
        for args, popup, lxx in self.row_sources:
            self._destination(*args, popup=popup, lxx=lxx or bool(self.row_lxx))
        self.row_sources.clear()
        self.row_lxx = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {}
        for name, value in attrs:
            values.setdefault(name, value)  # Match browser first-attribute semantics.
        line = self.embedded_at if self.embedded_at is not None else self.getpos()[0]
        if tag == "tr":
            self._finish_row()
            self.row_lxx = bool(LXX_CONTEXT.search(values.get("class") or ""))
        if tag == "a":
            self._finish_anchor()
            if "href" in values or "data-lexicon" in values:
                self.anchor = (values, line, [])
        if "data-popup-links" in values:
            self._json_links(values["data-popup-links"], line)
        popup = self.embedded_at is not None or any(
            k in values for k in ("data-lexicon", "data-popup-kind", "data-popup-links", "data-ref")
        )
        for name, href in values.items():
            if POPUP_URL_ATTRIBUTE.fullmatch(name) or (popup and name in {"data-href", "data-url", "data-link", "data-source-href", "data-source-url"}):
                self._destination(href, "", line, name, popup=True, lxx=name.startswith("data-lxx-"),
                                  lexicon=name.startswith("data-lexicon-"))
        if self.embedded_at is None and values.get("data-popup-text"):
            nested = _PopupHosts(self.policy, embedded_at=line)
            nested.feed(values["data-popup-text"])
            nested.close()
            self.measured += nested.measured
            self.popup_links += nested.popup_links
            self.findings.extend(nested.findings)

    def handle_data(self, data):
        if self.anchor is not None:
            self.anchor[2].append(data)
        if self.row_lxx is not None and LXX_CONTEXT.search(data):
            self.row_lxx = True

    def handle_endtag(self, tag):
        if tag == "a":
            self._finish_anchor()
        elif tag == "tr":
            self._finish_row()

    def close(self):
        super().close()
        self._finish_row()


def scan_popup_hosts(fragment: bytes, *, policy: PopupHostPolicy | None = None) -> dict:
    """Check saved Reader destinations in their link context, with no network."""
    parser = _PopupHosts(policy if policy is not None else load_popup_host_policy())
    parser.feed(fragment.decode("utf-8"))
    parser.close()
    return {"links_checked": parser.measured, "popup_links": parser.popup_links, "findings": parser.findings}


def check_rendered_popup_hosts(paths: list[Path]) -> dict:
    policy = load_popup_host_policy()
    findings = []
    measured = 0
    for path in paths:
        try:
            report = scan_popup_hosts(path.read_bytes(), policy=policy)
        except (OSError, UnicodeError):
            findings.append({"rule": "POPUP-SCAN-UNREADABLE", "path": str(path)})
            continue
        measured += report["links_checked"]
        findings.extend({**item, "path": str(path)} for item in report["findings"])
    return {
        "name": "rendered_popup_hosts",
        "state": "fail" if findings else "pass",
        "exit_code": int(bool(findings)),
        "detail": f"{measured} reader links checked across {len(paths)} fragments, {len(findings)} findings.",
        "findings": findings,
    }


class PendingInput(Exception):
    """A named input has not been produced; this is not an absence finding."""


class SavedInputs:
    """Bounded pinned data reads under caller-approved, canonical directory roots.

    No path or approval root is taken from the evidence itself. Parent directory
    descriptors and O_NOFOLLOW prevent symlink traversal; closing reads detect
    changed bytes, file replacements and root replacements. Repeated references
    reuse one observed buffer, then every unique input is re-read at close.
    """

    def __init__(self, roots: tuple[Path, ...]):
        self.roots = {}
        for root in roots:
            path = root.expanduser().resolve(strict=True)
            info = path.stat()
            if not stat.S_ISDIR(info.st_mode):
                raise ValueError("approved evidence root must be a directory")
            self.roots[path] = (info.st_dev, info.st_ino)
        self.cache: dict[Path, tuple[dict, bytes, tuple]] = {}
        self.read_bytes = 0

    def _path(self, value) -> Path:
        if not isinstance(value, str):
            raise ValueError("input path must be an absolute data-file name")
        path = Path(value)
        if not path.is_absolute() or ".." in path.parts or not any(path.is_relative_to(r) for r in self.roots):
            raise ValueError("input path outside caller-approved roots")
        return path

    def _physical(self, path: Path, size: int) -> tuple[bytes, tuple]:
        root = max((r for r in self.roots if path.is_relative_to(r)), key=lambda r: len(r.parts))
        now = root.stat()
        if (now.st_dev, now.st_ino) != self.roots[root]:
            raise ValueError("approved root moved during capture")
        relative = path.relative_to(root)
        if not relative.parts:
            raise ValueError("expected a data file, not an approved root")
        descriptors = []
        try:
            fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            descriptors.append(fd)
            opened_root = os.fstat(fd)
            if (opened_root.st_dev, opened_root.st_ino) != self.roots[root]:
                raise ValueError("approved root replaced before open")
            for part in relative.parts[:-1]:
                fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                descriptors.append(fd)
            fd = os.open(relative.parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
            descriptors.append(fd)
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode) or before.st_size != size:
                raise ValueError("input type/size differs from its pin")
            chunks, count = [], 0
            while True:
                part = os.read(fd, min(65536, size + 1 - count))
                if not part:
                    break
                count += len(part)
                self.read_bytes += len(part)
                if count > size or self.read_bytes > MAX_INPUT_READS:
                    raise ValueError("saved-input read bound exceeded")
                chunks.append(part)
            after = os.fstat(fd)
            identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
            if identity(before) != identity(after) or count != size:
                raise ValueError("input changed during read")
            return b"".join(chunks), identity(after)
        except FileNotFoundError as exc:
            raise PendingInput("named saved input not yet available") from exc
        finally:
            for fd in reversed(descriptors):
                os.close(fd)

    def read(self, reference: dict, expected_path: Path) -> bytes:
        if not isinstance(reference, dict) or set(reference) != {"path", "bytes", "sha256"}:
            raise ValueError("input needs an exact path/bytes/sha256 reference")
        path = self._path(reference["path"])
        if path != expected_path:
            raise ValueError("evidence path differs from independently selected current input")
        size, digest = reference["bytes"], reference["sha256"]
        if (type(size) is not int or not 0 <= size <= MAX_INPUT_FILE
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError("input pin invalid or oversized")
        if path in self.cache:
            previous, data, _ = self.cache[path]
            if reference != previous:
                raise ValueError("conflicting references to one current input")
            return data
        data, identity = self._physical(path, size)
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError("input bytes differ from the declared current pin")
        self.cache[path] = (dict(reference), data, identity)
        return data

    def closing_check(self) -> None:
        for path, (reference, original, identity) in self.cache.items():
            try:
                current, current_identity = self._physical(path, reference["bytes"])
            except PendingInput as exc:
                raise ValueError("current dependency disappeared before closing capture") from exc
            if current != original or current_identity != identity:
                raise ValueError("current dependency changed before closing capture")


def saved_mechanical_checks(week: int, week_dir: Path, evidence: dict | None,
                            *, current_inputs: dict | None = None,
                            approved_roots: tuple[Path, ...] = (),
                            generated_root: Path | None = None) -> dict:
    """Consume saved evidence without discovery, conversion, fetching or writing.

    The NATIVE OPERATOR supplies current_inputs and approved_roots independently
    of evidence. current_inputs contains word_cards[kind] path maps and a
    resources path map plus lesson_reading. They are normal run/config context,
    not another checklist/state file. Source paths are canonical for week/kind;
    page/template/data/extra dependencies and evidence paths must match that
    context exactly. This API seam does not wire the native CLI or producer.

    Evidence: {week, week_dir, word_cards:{kind:{inventory,capture,source_files,
    dependencies}}, resources:{tracker,reading,static,fresh,stored,served,evidence}}.
    Every file is a pinned reference; missing inventory/capture/output may be
    None. Accepted validator schemas are unchanged. Both guide and insights plus
    resources are required for the WHOLE mechanical scope to be called pass.
    A narrower valid scope remains incomplete and cannot mean week readiness.
    """
    result = {"state": "not_run", "word_cards": {}, "resources": {"status": "not_run"},
              "findings": [], "inputs": [], "read_bytes": 0,
              "publication_authorized": False,
              "limits": ["Caller-approved current-file context and supplied review/capture provenance; no authentication of scholarly judgement",
                         "No native producer/CLI installation, browser execution, video discovery or publication authority",
                         "Legacy Greek nested-only diagnostic remains separate; it is not a rule of this source-specific check"]}
    if evidence is None:
        result["findings"].append("SAVED_CHECK_INPUTS_NOT_SUPPLIED")
        return result
    reader = None
    try:
        if not isinstance(evidence, dict) or set(evidence) != {"week", "week_dir", "word_cards", "resources"}:
            raise ValueError("saved inputs must contain identities and evidence, not a precomputed PASS")
        root = week_dir.expanduser().resolve()
        if not root.is_dir() or not root.name.startswith(f"Week_{week:02d}_"):
            raise ValueError("week/root context must name the selected canonical week directory")
        if evidence["week"] != week or evidence["week_dir"] != str(root):
            raise ValueError("saved evidence belongs to a different week/root")
        if not isinstance(current_inputs, dict) or set(current_inputs) != {"word_cards", "resources", "lesson_reading"}:
            raise ValueError("independent current input context is required")
        if not isinstance(evidence["word_cards"], dict) or not isinstance(current_inputs["word_cards"], dict):
            raise ValueError("word-card scopes must be objects")
        reader = SavedInputs(approved_roots)
        # Fixed trusted code imports, never a module/plugin named by evidence.
        from verification import word_card_coverage, weekly_resource_selection, review_evidence
        for module in (word_card_coverage, weekly_resource_selection, review_evidence):
            if Path(module.__file__).resolve().parent != ROOT / "verification":
                raise ValueError("validator import is outside this source installation")
        full_sources = review_evidence.content_paths(root, week)
        valid_kinds = {"study-guide": full_sources[:-1], "insights": full_sources[-1:]}

        def read_json(ref, path):
            return json.loads(reader.read(ref, path))

        def missing(message):
            return {"status": "not_run", "findings": [message]}

        for kind in evidence["word_cards"]:
            if kind not in valid_kinds:
                raise ValueError("unsupported word-card content kind")
        for kind, paths in valid_kinds.items():
            pack = evidence["word_cards"].get(kind)
            if pack is None:
                result["word_cards"][kind] = missing("WORD_SCOPE_NOT_SUPPLIED")
                continue
            try:
                if not isinstance(pack, dict) or set(pack) != {"inventory", "capture", "source_files", "dependencies"}:
                    raise ValueError("invalid word-card input bundle")
                if pack["inventory"] is None or pack["capture"] is None:
                    raise PendingInput("reviewed authored inventory/after-script capture not yet supplied")
                context = current_inputs["word_cards"].get(kind)
                if not isinstance(context, dict):
                    raise ValueError("current word-card file context missing")
                dependencies = pack["dependencies"]
                if not isinstance(dependencies, dict) or not {"page", "template", "data"} <= dependencies.keys():
                    raise ValueError("page/template/data dependency references required")
                if set(context) != {"inventory", "capture", *dependencies}:
                    raise ValueError("current word dependency population differs")
                sources = pack["source_files"]
                if not isinstance(sources, list) or len(sources) != len(paths):
                    raise ValueError("full canonical author-source population required")
                if kind == "study-guide" and {p.name for p in paths[0].parent.glob("*.md")} != {p.name for p in paths}:
                    raise ValueError("canonical guide source population differs")
                source_parts = [reader.read(ref, path) for ref, path in zip(sources, paths)]
                if any(not part.strip() for part in source_parts):
                    raise PendingInput("canonical author source has not been written")
                current_source = b"\n\n".join(source_parts)
                bindings = {"source": hashlib.sha256(current_source).hexdigest()}
                for key, ref in dependencies.items():
                    if key == "source":
                        raise ValueError("source dependency is derived from canonical author bytes")
                    data = reader.read(ref, Path(context[key]))
                    bindings[key] = hashlib.sha256(data).hexdigest()
                inventory = read_json(pack["inventory"], Path(context["inventory"]))
                capture = read_json(pack["capture"], Path(context["capture"]))
                scope = {"document": f"week-{week}", "kind": kind,
                         "sections": [p.stem for p in paths] if kind == "study-guide" else ["Weekly_Insights"]}
                result["word_cards"][kind] = word_card_coverage.evaluate(inventory, capture, bindings=bindings, scope=scope)
            except PendingInput as exc:
                result["word_cards"][kind] = missing(str(exc))

        pack = evidence["resources"]
        if pack is not None:
            try:
                required = {"tracker", "reading", "static", "fresh", "stored", "served", "evidence"}
                if not isinstance(pack, dict) or set(pack) != required:
                    raise ValueError("invalid resource input bundle")
                context = current_inputs["resources"]
                if not isinstance(context, dict) or set(context) != required - {"reading"}:
                    raise ValueError("current resource file context missing")
                if generated_root is not None and Path(context["stored"]) != generated_root.resolve() / "resources.html":
                    raise ValueError("stored resources differ from this native rendered target")
                reading = current_inputs["lesson_reading"]
                if not isinstance(reading, str) or not reading.strip():
                    raise PendingInput("official current-reading context not supplied by operator")
                if pack["reading"] != reading:
                    raise ValueError("resource reading differs from current official context")
                tracker_path = Path(context["tracker"])
                if tracker_path not in {root / "01_Weekly_Resources/VIDEO_URL_TRACKER.md",
                                        root / "Video_Resources/VIDEO_URL_TRACKER.md"}:
                    raise ValueError("tracker is outside the selected week's canonical locations")
                tracker = reader.read(pack["tracker"], tracker_path).decode("utf-8")
                if not tracker.strip() or not weekly_resource_selection.tracker_population(tracker):
                    result["resources"] = {"status": "not_run", "denominator": 0, "accounted": 0,
                                           "findings": ["RESOURCE_TRACKER_UNWRITTEN_OR_NO_DECLARED_ROWS"]}
                elif any(pack[key] is None for key in ("static", "fresh", "stored", "served", "evidence")):
                    result["resources"] = weekly_resource_selection.reconcile_rows(tracker, reading, {}, None, None, None, None)
                else:
                    static_data = read_json(pack["static"], Path(context["static"]))
                    if not isinstance(static_data, dict):
                        raise ValueError("current static media data must be an object")
                    fresh, stored, served = [reader.read(pack[key], Path(context[key])).decode("utf-8")
                                            for key in ("fresh", "stored", "served")]
                    if any(not html.strip() for html in (fresh, stored, served)):
                        result["resources"] = weekly_resource_selection.reconcile_rows(
                            tracker, reading, static_data, None, None, None, None)
                        result["resources"]["findings"].append("RESOURCE_RENDER_NOT_YET_WRITTEN")
                    else:
                        rows = read_json(pack["evidence"], Path(context["evidence"]))
                        result["resources"] = weekly_resource_selection.reconcile_rows(
                            tracker, reading, static_data, fresh, stored, served, rows)
            except PendingInput as exc:
                result["resources"] = missing(str(exc))
        reader.closing_check()
        states = [r["status"] for r in result["word_cards"].values()] + [result["resources"]["status"]]
        result["state"] = ("fail" if "fail" in states else "pass" if all(s == "pass" for s in states)
                           else "not_run" if all(s == "not_run" for s in states) else "incomplete")
    except (OSError, ValueError, TypeError, KeyError, AttributeError, ImportError) as exc:
        result["state"] = "fail"
        result["findings"].append(f"SAVED_CHECK_INPUT_INVALID:{type(exc).__name__}:{exc}")
    if reader is not None:
        result["inputs"] = [r for r, _, _ in reader.cache.values()]
        result["read_bytes"] = reader.read_bytes
    return result


def run_check(name: str, command: list[str]) -> dict:
    """Execute one local check and preserve its bounded, reproducible outcome."""
    try:
        completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"name": name, "state": "unmeasured", "detail": f"{type(exc).__name__}: {exc}"}
    output = ((completed.stdout or "") + (completed.stderr or "")).strip()
    return {
        "name": name,
        "state": "pass" if completed.returncode == 0 else "fail",
        "exit_code": completed.returncode,
        "detail": output[-1600:] or "no output",
    }


def evaluate(week: int, week_dir: Path, stage: str, rendered_dir: Path | None = None,
             *, saved_check_inputs: dict | None = None, current_inputs: dict | None = None,
             approved_roots: tuple[Path, ...] = ()) -> dict:
    """Return a machine-readable stage result without changing any project file."""
    week_dir = week_dir.expanduser().resolve()
    result = {
        "week": week,
        "week_dir": str(week_dir),
        "stage": stage,
        "ready": False,
        "publication_authorized": False,
        "checks": [],
        "blockers": [],
    }
    if not week_dir.is_dir() or not week_dir.name.startswith(f"Week_{week:02d}_"):
        result["blockers"].append("--week-dir must be the exact matching Week_NN_* source root")
        return result

    python = sys.executable
    if stage == "prepare":
        result["checks"].append(run_check(
            "lesson_start", [python, "verification/gate_lesson_start.py", "--week", str(week)]))
        result["checks"].append(run_check(
            "preparation_evidence", [python, "verification/review_evidence.py", "--week", str(week),
                                       "--week-dir", str(week_dir), "--stage", "prepare", "--json"]))
    else:
        if rendered_dir is None:
            result["blockers"].append("--rendered-dir is required after generation")
        else:
            rendered_dir = rendered_dir.expanduser().resolve()
            html_files = sorted(rendered_dir.glob("*.html")) if rendered_dir.is_dir() else []
            if not html_files:
                result["blockers"].append("rendered output unavailable: expected at least one HTML fragment")
            else:
                result["rendered_dir"] = str(rendered_dir)
                popup_hosts = check_rendered_popup_hosts(html_files)
                result["checks"].append(run_check(
                    "rendered_scripture_targets",
                    [python, "verification/check_link_targets.py", "--dir", str(rendered_dir),
                     "--require-blb-bible"]))
                result["checks"].append(popup_hosts)
        if stage == "handoff":
            result["checks"].append(run_check(
                "handoff_evidence", [python, "verification/review_evidence.py", "--week", str(week),
                                     "--week-dir", str(week_dir), "--stage", "handoff", "--json"]))

    failed = [check["name"] for check in result["checks"] if check["state"] != "pass"]
    if failed:
        result["blockers"].append("checks not current: " + ", ".join(failed))
    result["ready"] = bool(result["checks"]) and not result["blockers"]
    if saved_check_inputs is not None:
        result["legacy_ready"] = result["ready"]
        result["preparation_can_continue"] = result["ready"]
        result["mechanical_evidence"] = (saved_mechanical_checks(
            week, week_dir, saved_check_inputs, current_inputs=current_inputs, approved_roots=approved_roots,
            generated_root=rendered_dir)
            if stage in ("rendered", "handoff") else
            {"state": "not_run", "findings": ["SAVED_CHECKS_APPLY_AFTER_GENERATION"]})
        state = result["mechanical_evidence"]["state"]
        result["mechanical_complete"] = state == "pass"
        result["ready"] = result["legacy_ready"] and result["mechanical_complete"]
        result["readiness_scope"] = "Legacy stage checks and separately reported saved mechanical evidence; not whole-lesson or publication readiness"
        # Pending evidence does not block ordinary prose/static preparation.
        # Actual failures remain explicit blockers for this opted-in check.
        if state == "fail":
            result["blockers"].append("opted-in saved mechanical evidence failed")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--week", type=int, required=True)
    parser.add_argument("--week-dir", type=Path, required=True)
    parser.add_argument("--stage", choices=("prepare", "rendered", "handoff"), required=True)
    parser.add_argument("--rendered-dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = evaluate(args.week, args.week_dir, args.stage, args.rendered_dir)
    except PopupHostPolicyError as exc:
        if args.json:
            print(json.dumps({
                "week": args.week, "week_dir": str(args.week_dir), "stage": args.stage,
                "ready": False, "publication_authorized": False, "checks": [], "blockers": [str(exc)],
            }, indent=2))
        else:
            print(str(exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Week {args.week} {args.stage}: {'READY FOR NEXT STAGE' if result['ready'] else 'NOT READY'}")
        for check in result["checks"]:
            print(f"  {check['state'].upper():10} {check['name']}")
            if check["state"] != "pass":
                print("    " + check["detail"].replace("\n", "\n    "))
        for blocker in result["blockers"]:
            print(f"  BLOCKER {blocker}")
        print("This result is not publication authority.")
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
