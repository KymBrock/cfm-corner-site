#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
    (re.compile(r"^Song\s+", re.I), "Song of Solomon "),
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
    m = re.match(r"^(.*?\d+:\d+)-\d+$", base)
    if m:
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

    total = 0
    for path in sorted(file_paths):
        problems = check_file(path)
        if not problems:
            continue
        total += len(problems)
        print(f"\n{path.relative_to(ROOT)}")
        for problem in problems[:20]:
            print(f"  - {problem}")
        if len(problems) > 20:
            print(f"  - ... {len(problems) - 20} more")

    if total == 0:
        print("No popup-link issues detected.")
    else:
        print(f"\nFound {total} potential popup-link issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
