#!/usr/bin/env python3
"""Trim scripture-verses.json for Cloudflare Pages previews.

Cloudflare Pages rejects files over 25 MiB; the full verse database is ~92 MiB.
This scans the BUILT site (public/) for every scripture reference that could
trigger a hover popup — data-ref attributes, scripture-site links, and textual
citations (the same forms baseof.html's normalizeRef/getReferenceCandidates
resolve) — and overwrites public/data/scripture-verses.json with only those
entries. static/data/ and production deploys are untouched.

Used by scripts/deploy-preview.sh. Run from the repo root.
"""
import json
import re
import sys
from pathlib import Path

PUB = Path("public")
SRC = Path("static/data/scripture-verses.json")

db = json.load(SRC.open())

# Full book names, derived from the database's own keys.
books = set()
key_re = re.compile(r"^(.*?)\s+\d+:\d")
for k in db:
    m = key_re.match(k)
    if m:
        books.add(m.group(1))

# Mirror of refAliases in themes/cfm/layouts/_default/baseof.html
ALIASES = {
    "Ps.": "Psalms", "Psa.": "Psalms", "Psalm": "Psalms", "Prov.": "Proverbs",
    "Eccl.": "Ecclesiastes", "Song": "Song of Solomon", "Ex.": "Exodus",
    "Lev.": "Leviticus", "Num.": "Numbers", "Deut.": "Deuteronomy",
    "Josh.": "Joshua", "Judg.": "Judges", "1 Sam.": "1 Samuel",
    "2 Sam.": "2 Samuel", "1 Kgs.": "1 Kings", "2 Kgs.": "2 Kings",
    "1 Chr.": "1 Chronicles", "2 Chr.": "2 Chronicles", "Neh.": "Nehemiah",
    "Esth.": "Esther", "Isa.": "Isaiah", "Jer.": "Jeremiah",
    "Ezek.": "Ezekiel", "Hos.": "Hosea", "Obad.": "Obadiah",
    "Zech.": "Zechariah", "Mal.": "Malachi", "Matt.": "Matthew",
    "Jn.": "John", "Rom.": "Romans", "1 Cor.": "1 Corinthians",
    "2 Cor.": "2 Corinthians", "Phil.": "Philippians", "Col.": "Colossians",
    "1 Thes.": "1 Thessalonians", "2 Thes.": "2 Thessalonians",
    "1 Tim.": "1 Timothy", "2 Tim.": "2 Timothy", "Philem.": "Philemon",
    "1 Pet.": "1 Peter", "2 Pet.": "2 Peter", "Rev.": "Revelation",
    "1 Ne.": "1 Nephi", "2 Ne.": "2 Nephi", "Hel.": "Helaman",
    "Moro.": "Moroni", "Doctrine and Covenants": "D&C",
    "JST Ex.": "JST Exodus", "JST Gen.": "JST Genesis",
    "JST Matt.": "JST Matthew",
}

names = sorted(books | set(ALIASES), key=len, reverse=True)
name_pat = "|".join(re.escape(n) for n in names)
# Book + chapter:verse(-verse)?  OR  Book + bare chapter (for the
# chapter-reference fallback in getVerse()).
ref_re = re.compile(r"(?:%s)\s+\d+(?::\d+(?:-\d+)?)?" % name_pat)
dataref_re = re.compile(r'data-ref="([^"]+)"')

def normalize(ref):
    out = re.sub(r"\s+", " ", ref.strip()).replace("–", "-").replace("—", "-")
    for alias, full in ALIASES.items():
        if out.startswith(alias + " "):
            out = full + " " + out[len(alias) + 1:]
            break
    return out

found = set()
for page in PUB.rglob("*.html"):
    html = page.read_text(errors="ignore")
    html = html.replace("–", "-").replace("—", "-").replace("&nbsp;", " ")
    for m in dataref_re.finditer(html):
        found.add(normalize(m.group(1)))
    for m in ref_re.finditer(html):
        found.add(normalize(m.group(0)))

# Expand to db keys, following getReferenceCandidates(): exact key, the
# Psalm/Psalms and D&C variants, a range's opening verse, and one key per
# bare-chapter reference so the chapter fallback still fires.
by_chapter = {}
for k in db:
    ch = k.split(":")[0]
    by_chapter.setdefault(ch, k if ":" in k else None)
    if ":" in k and (by_chapter[ch] is None or k < by_chapter[ch]):
        by_chapter[ch] = k

wanted = set()
for ref in found:
    variants = {ref}
    if ref.startswith("Psalms "):
        variants.add("Psalm " + ref[7:])
    if ref.startswith("Psalm "):
        variants.add("Psalms " + ref[6:])
    if ref.startswith("D&C "):
        variants.add("Doctrine and Covenants " + ref[4:])
    for v in set(variants):
        m = re.match(r"^(.*?\d+:\d+)-\d+$", v)
        if m:
            variants.add(m.group(1))
    for v in variants:
        if v in db:
            wanted.add(v)
        elif ":" not in v and v in by_chapter and by_chapter[v]:
            wanted.add(by_chapter[v])  # bare chapter -> keep one verse key

out = {k: db[k] for k in wanted}
dest = PUB / "data" / "scripture-verses.json"
dest.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
size_mb = dest.stat().st_size / 1024 / 1024
print(f"scripture-verses.json: {len(out)}/{len(db)} entries kept, {size_mb:.1f} MiB")
if size_mb > 24:
    sys.exit("still over Cloudflare's 25 MiB limit")
