#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTURE_DB = json.loads((ROOT / "static/data/scripture-verses.json").read_text())


ALIAS_RULES = [
    (re.compile(r"^Ps\.\s+", re.I), "Psalms "),
    (re.compile(r"^Psa\.\s+", re.I), "Psalms "),
    (re.compile(r"^Psalm\s+", re.I), "Psalms "),
    (re.compile(r"^Prov\.\s+", re.I), "Proverbs "),
    (re.compile(r"^Eccl\.\s+", re.I), "Ecclesiastes "),
    (re.compile(r"^Song\s+(?=\d)", re.I), "Song of Solomon "),
    (re.compile(r"^Ex\.\s+", re.I), "Exodus "),
    (re.compile(r"^Lev\.\s+", re.I), "Leviticus "),
    (re.compile(r"^Num\.\s+", re.I), "Numbers "),
    (re.compile(r"^Deut\.\s+", re.I), "Deuteronomy "),
    (re.compile(r"^Josh\.\s+", re.I), "Joshua "),
    (re.compile(r"^Judg\.\s+", re.I), "Judges "),
    (re.compile(r"^1\s+Sam\.\s+", re.I), "1 Samuel "),
    (re.compile(r"^2\s+Sam\.\s+", re.I), "2 Samuel "),
    (re.compile(r"^1\s+Kgs\.\s+", re.I), "1 Kings "),
    (re.compile(r"^2\s+Kgs\.\s+", re.I), "2 Kings "),
    (re.compile(r"^1\s+Chr\.\s+", re.I), "1 Chronicles "),
    (re.compile(r"^2\s+Chr\.\s+", re.I), "2 Chronicles "),
    (re.compile(r"^Neh\.\s+", re.I), "Nehemiah "),
    (re.compile(r"^Esth\.\s+", re.I), "Esther "),
    (re.compile(r"^Isa\.\s+", re.I), "Isaiah "),
    (re.compile(r"^Jer\.\s+", re.I), "Jeremiah "),
    (re.compile(r"^Ezek\.\s+", re.I), "Ezekiel "),
    (re.compile(r"^Hos\.\s+", re.I), "Hosea "),
    (re.compile(r"^Obad\.\s+", re.I), "Obadiah "),
    (re.compile(r"^Zech\.\s+", re.I), "Zechariah "),
    (re.compile(r"^Mal\.\s+", re.I), "Malachi "),
    (re.compile(r"^Matt\.\s+", re.I), "Matthew "),
    (re.compile(r"^Jn\.\s+", re.I), "John "),
    (re.compile(r"^Rom\.\s+", re.I), "Romans "),
    (re.compile(r"^1\s+Cor\.\s+", re.I), "1 Corinthians "),
    (re.compile(r"^2\s+Cor\.\s+", re.I), "2 Corinthians "),
    (re.compile(r"^Phil\.\s+", re.I), "Philippians "),
    (re.compile(r"^Col\.\s+", re.I), "Colossians "),
    (re.compile(r"^1\s+Thes\.\s+", re.I), "1 Thessalonians "),
    (re.compile(r"^2\s+Thes\.\s+", re.I), "2 Thessalonians "),
    (re.compile(r"^1\s+Tim\.\s+", re.I), "1 Timothy "),
    (re.compile(r"^2\s+Tim\.\s+", re.I), "2 Timothy "),
    (re.compile(r"^Philem\.\s+", re.I), "Philemon "),
    (re.compile(r"^1\s+Pet\.\s+", re.I), "1 Peter "),
    (re.compile(r"^2\s+Pet\.\s+", re.I), "2 Peter "),
    (re.compile(r"^Rev\.\s+", re.I), "Revelation "),
    (re.compile(r"^1\s+Ne\.\s+", re.I), "1 Nephi "),
    (re.compile(r"^2\s+Ne\.\s+", re.I), "2 Nephi "),
    (re.compile(r"^Hel\.\s+", re.I), "Helaman "),
    (re.compile(r"^Moro\.\s+", re.I), "Moroni "),
    (re.compile(r"^Doc(?:trine)?\s+and\s+Covenants\s+", re.I), "D&C "),
    (re.compile(r"^JST\s+Ex\.\s+", re.I), "JST Exodus "),
    (re.compile(r"^JST\s+Gen\.\s+", re.I), "JST Genesis "),
    (re.compile(r"^JST\s+Matt\.\s+", re.I), "JST Matthew "),
]


DATA_REF_RE = re.compile(r'data-ref="([^"]+)"')
SUSPICIOUS_RE = re.compile(
    r"(?<![1-4]\s)\b(?:Corinthians|Nephi|Timothy|Thessalonians|Samuel|Kings|Chronicles|Peter)\s+\d+:\d+(?:[-–]\d+)?\b"
)
MISSING_BOOK_RE = re.compile(r"\((?:JST\s+)?\d+:\d+(?:[-–]\d+)?\)")


def normalize_ref(ref: str) -> str:
    out = ref.strip()
    out = out.replace("–", "-").replace("—", "-")
    out = re.sub(r"\s+", " ", out)
    for pattern, repl in ALIAS_RULES:
      out = pattern.sub(repl, out)
    return out


def candidates(ref: str) -> list[str]:
    base = normalize_ref(ref)
    out = [base]
    if base.startswith("Psalms "):
        out.append(base.replace("Psalms ", "Psalm ", 1))
    if base.startswith("Psalm "):
        out.append(base.replace("Psalm ", "Psalms ", 1))
    if base.startswith("D&C "):
        out.append(base.replace("D&C ", "Doctrine and Covenants ", 1))
    if base.startswith("Doctrine and Covenants "):
        out.append(base.replace("Doctrine and Covenants ", "D&C ", 1))
    if base.startswith("Joseph Smith-Matthew "):
        out.append(base.replace("Joseph Smith-Matthew ", "Joseph Smith—Matthew ", 1))
    if base.startswith("Joseph Smith—Matthew "):
        out.append(base.replace("Joseph Smith—Matthew ", "Joseph Smith-Matthew ", 1))
    if base.startswith("Joseph Smith-History "):
        out.append(base.replace("Joseph Smith-History ", "Joseph Smith—History ", 1))
    if base.startswith("Joseph Smith—History "):
        out.append(base.replace("Joseph Smith—History ", "Joseph Smith-History ", 1))
    m = re.match(r"^(.*?\d+:\d+)-\d+$", base)
    if m:
        out.append(m.group(1))
    # B3 r2: judge a list or a range by its first reference, the way the popup opens it.
    #   "Jeremiah 2:18, 36" → "Jeremiah 2:18";  "Proverbs 22:17-24:22" → "Proverbs 22:17";
    #   "Genesis 37-50" (chapters) → "Genesis 37".
    m = re.match(r"^(.*?\d+(?::\d+)?)\s*[,;]", base)
    if m:
        out.append(m.group(1))
    m = re.match(r"^(.*?\d+:\d+)-\d+:\d+$", base)
    if m:
        out.append(m.group(1))
    m = re.match(r"^(.*?\s\d+)-\d+$", base)
    if m and ":" not in base:
        out.append(m.group(1))
    seen = []
    for item in out:
        if item not in seen:
            seen.append(item)
    return seen


def resolves(ref: str) -> bool:
    for candidate in candidates(ref):
        if candidate in SCRIPTURE_DB:
            return True
        if re.match(r"^\S.* \d+$", candidate):
            chapter_prefix = candidate + ":"
            if any(key.startswith(chapter_prefix) for key in SCRIPTURE_DB):
                return True
    return False


def check_file(path: Path) -> list[str]:
    text = path.read_text(errors="ignore")
    problems: list[str] = []

    for ref in DATA_REF_RE.findall(text):
        if "${" in ref:
            continue
        # B3: decode entities first (`D&amp;C 77:2-4` is `D&C 77:2-4`). Skip only refs
        # with NO digit at all: word data-refs such as `qərê (קְרֵי)` or `Leitwort` are not
        # scripture. Anything with a digit is judged, so corrupted refs like `1 <a href=`
        # (W17) and a bare `11` (Egypt guide) still fail. (r2.)
        ref = html.unescape(ref)
        if not re.search(r"[0-9]", ref):
            continue
        if not resolves(ref):
            problems.append(f"unresolved data-ref: {ref}")

    for match in SUSPICIOUS_RE.findall(text):
        problems.append(f"suspicious missing numeric prefix: {match}")

    for match in MISSING_BOOK_RE.findall(text):
        problems.append(f"missing book name: {match[1:-1]}")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Check popup-link coverage and likely scripture citation mistakes.")
    parser.add_argument("paths", nargs="*", help="Optional files or directories to scan.")
    args = parser.parse_args()

    roots = [ROOT / "content", ROOT / "static/content"]
    file_paths = []
    scan_targets = [ROOT / p for p in args.paths] if args.paths else roots

    for target in scan_targets:
        if target.is_file() and target.suffix in {".md", ".html"}:
            file_paths.append(target)
            continue
        if target.is_dir():
            file_paths.extend(p for p in target.rglob("*") if p.suffix in {".md", ".html"})

    if not file_paths:
        # B3: nothing scanned is not a pass. Exit 2 = cannot vouch.
        print("No files scanned — check the path. Exit 2 (cannot vouch).")
        return 2

    total = 0
    blocking = 0
    for path in sorted(file_paths):
        problems = check_file(path)
        if not problems:
            continue
        total += len(problems)
        blocking += sum(1 for p in problems if p.startswith("unresolved data-ref"))
        print(f"\n{path.relative_to(ROOT)}")
        for problem in problems[:20]:
            print(f"  - {problem}")
        if len(problems) > 20:
            print(f"  - ... {len(problems) - 20} more")

    if total == 0:
        print("No popup-link issues detected.")
    else:
        print(f"\nFound {total} potential popup-link issues.")
    # B3 (gap audit 2026-11-27): a popup whose scripture ref does not resolve is a broken
    # popup a reader sees — exit 1. "missing book name" and "suspicious prefix" are
    # pattern guesses with many correct hits (e.g. "(66:20)" after the book is named),
    # so they stay advisory and do not fail the run.
    if blocking:
        print(f"{blocking} unresolved scripture popup ref(s) — exit 1.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
