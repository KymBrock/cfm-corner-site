#!/usr/bin/env python3
"""
Scripture Usage Radar

Analyzes scripture usage in weekly content and generates editorial QA reports.

Usage:
    python scripts/scripture-usage-radar.py --week 12
    python scripts/scripture-usage-radar.py --week 12 --output reports/week12_radar.md
    python scripts/scripture-usage-radar.py --path static/content/week12/

Reports:
    - Unique references and total citations
    - Section-level scripture coverage
    - Most-used references
    - Expected anchor passages (missing/present)
    - Cross-site reuse from scripture-backlinks.json
    - Theme concentration warnings
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path


# Configuration
CONTENT_DIR = Path(__file__).parent.parent / "static" / "content"
BACKLINKS_PATH = Path(__file__).parent.parent / "static" / "data" / "scripture-backlinks.json"
EXPECTED_PASSAGES_PATH = Path(__file__).parent.parent / "static" / "data" / "expected-passages.json"
REPORTS_DIR = Path(__file__).parent.parent / "reports"

# Canon classification patterns
CANON_PATTERNS = {
    "OT": [
        r"^Genesis", r"^Exodus", r"^Leviticus", r"^Numbers", r"^Deuteronomy",
        r"^Joshua", r"^Judges", r"^Ruth", r"^1 Samuel", r"^2 Samuel",
        r"^1 Kings", r"^2 Kings", r"^1 Chronicles", r"^2 Chronicles",
        r"^Ezra", r"^Nehemiah", r"^Esther", r"^Job", r"^Psalm",
        r"^Proverbs", r"^Ecclesiastes", r"^Song of Solomon", r"^Isaiah",
        r"^Jeremiah", r"^Lamentations", r"^Ezekiel", r"^Daniel",
        r"^Hosea", r"^Joel", r"^Amos", r"^Obadiah", r"^Jonah", r"^Micah",
        r"^Nahum", r"^Habakkuk", r"^Zephaniah", r"^Haggai", r"^Zechariah",
        r"^Malachi",
    ],
    "NT": [
        r"^Matthew", r"^Mark", r"^Luke", r"^John(?! \d)",  # John but not 1/2/3 John
        r"^Acts", r"^Romans", r"^1 Corinthians", r"^2 Corinthians",
        r"^Galatians", r"^Ephesians", r"^Philippians", r"^Colossians",
        r"^1 Thessalonians", r"^2 Thessalonians", r"^1 Timothy", r"^2 Timothy",
        r"^Titus", r"^Philemon", r"^Hebrews", r"^James",
        r"^1 Peter", r"^2 Peter", r"^1 John", r"^2 John", r"^3 John",
        r"^Jude", r"^Revelation",
    ],
    "BoM": [
        r"^1 Nephi", r"^2 Nephi", r"^Jacob", r"^Enos", r"^Jarom", r"^Omni",
        r"^Words of Mormon", r"^Mosiah", r"^Alma", r"^Helaman",
        r"^3 Nephi", r"^4 Nephi", r"^Mormon", r"^Ether", r"^Moroni",
    ],
    "D&C": [
        r"^D&C", r"^Doctrine and Covenants", r"^OD",  # Official Declarations
    ],
    "PGP": [
        r"^Moses", r"^Abraham", r"^Joseph Smith[—\-]Matthew",
        r"^Joseph Smith[—\-]History", r"^Articles of Faith",
    ],
}


class SectionAwareRefExtractor(HTMLParser):
    """HTML parser that extracts data-ref attributes with section context."""

    SKIP_CHARS = {"⊞", "⊟", "▶︎", "▼", "◀", "▲", "▶", "►", "◄", "︎"}

    def __init__(self):
        super().__init__()
        self.refs = []  # List of {ref, section, subsection}
        self.current_section = None
        self.current_subsection = None

        # Track section-header divs (insights/resources)
        self.in_section_header = False
        self.section_header_depth = 0

        # Track sg-accordion-section divs (study guides)
        self.in_sg_accordion = False
        self.sg_accordion_depth = 0
        self.in_sg_section_title = False

        # Track sg-sub-accordion buttons (study guides sub-sections)
        self.in_sg_sub_accordion = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        css_class = attrs_dict.get("class", "")

        # insights/resources: <div class="section-header">
        if tag == "div" and "section-header" in css_class:
            self.in_section_header = True
            self.section_header_depth = 1
        elif self.in_section_header and tag == "div":
            self.section_header_depth += 1

        # study-guide: <div class="sg-accordion-section">
        if tag == "div" and "sg-accordion-section" in css_class:
            self.in_sg_accordion = True
            self.sg_accordion_depth = 1
        elif self.in_sg_accordion and tag == "div":
            self.sg_accordion_depth += 1

        # study-guide: <span class="sg-section-title">
        if tag == "span" and "sg-section-title" in css_class:
            self.in_sg_section_title = True

        # study-guide sub-sections: <button class="sg-sub-accordion">
        if tag == "button" and "sg-sub-accordion" in css_class:
            self.in_sg_sub_accordion = True

        # Extract data-ref
        if "data-ref" in attrs_dict:
            ref = attrs_dict["data-ref"]
            if ref:
                self.refs.append({
                    "ref": normalize_ref(ref),
                    "section": self.current_section,
                    "subsection": self.current_subsection,
                })

    def handle_endtag(self, tag):
        if self.in_section_header and tag == "div":
            self.section_header_depth -= 1
            if self.section_header_depth == 0:
                self.in_section_header = False

        if self.in_sg_accordion and tag == "div":
            self.sg_accordion_depth -= 1
            if self.sg_accordion_depth == 0:
                self.in_sg_accordion = False

        if self.in_sg_section_title and tag == "span":
            self.in_sg_section_title = False

        if self.in_sg_sub_accordion and tag == "button":
            self.in_sg_sub_accordion = False

    def handle_data(self, data):
        text = data.strip()
        if not text or text in self.SKIP_CHARS:
            return

        if self.in_section_header:
            self.current_section = text
            self.current_subsection = None
        elif self.in_sg_section_title:
            self.current_section = text
            self.current_subsection = None
        elif self.in_sg_sub_accordion:
            self.current_subsection = text


def normalize_ref(ref: str) -> str:
    """Normalize a scripture reference."""
    ref = ref.strip()
    ref = re.sub(r'[–—−]', '-', ref)
    ref = re.sub(r'\s*-\s*', '-', ref)
    ref = re.sub(r'\s+', ' ', ref)
    return ref


def classify_canon(ref: str) -> str:
    """Classify a reference into canon category."""
    for canon, patterns in CANON_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern, ref, re.IGNORECASE):
                return canon
    return "Other"


def extract_book(ref: str) -> str:
    """Extract book name from reference."""
    match = re.match(r'^(\d?\s?[A-Za-z\s&]+?)(?:\s+\d|$)', ref)
    if match:
        return match.group(1).strip()
    return ref


def extract_chapter(ref: str) -> str:
    """Extract book and chapter from reference."""
    match = re.match(r'^(.+?)\s+(\d+)', ref)
    if match:
        return f"{match.group(1)} {match.group(2)}"
    return ref


def load_backlinks() -> dict:
    """Load scripture-backlinks.json."""
    if BACKLINKS_PATH.exists():
        with open(BACKLINKS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def load_expected_passages() -> dict:
    """Load expected anchor passages per week."""
    if EXPECTED_PASSAGES_PATH.exists():
        with open(EXPECTED_PASSAGES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def extract_refs_from_file(filepath: Path) -> list:
    """Extract all data-ref attributes from an HTML file."""
    try:
        content = filepath.read_text(encoding='utf-8')
        parser = SectionAwareRefExtractor()
        parser.feed(content)
        return parser.refs
    except Exception as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return []


def analyze_week(week_num: int, content_dir: Path = CONTENT_DIR) -> dict:
    """Analyze scripture usage for a week."""
    week_dir = content_dir / f"week{week_num}"
    if not week_dir.exists():
        # Try zero-padded
        week_dir = content_dir / f"week{week_num:02d}"
    if not week_dir.exists():
        return {"error": f"Week directory not found: week{week_num}"}

    return analyze_path(week_dir, week_num)


def analyze_path(path: Path, week_num: int = None) -> dict:
    """Analyze scripture usage for a path (file or directory)."""
    if path.is_file():
        files = [path]
    else:
        files = list(path.glob("*.html"))

    # Collect all references
    all_refs = []
    refs_by_file = {}
    refs_by_section = defaultdict(list)

    for filepath in files:
        file_refs = extract_refs_from_file(filepath)
        refs_by_file[filepath.name] = file_refs
        all_refs.extend(file_refs)

        for ref_info in file_refs:
            section = ref_info.get("section") or "No Section"
            refs_by_section[section].append(ref_info["ref"])

    # Deduplicate refs
    unique_refs = set(r["ref"] for r in all_refs)
    total_citations = len(all_refs)

    # Count by reference
    ref_counts = defaultdict(int)
    for ref_info in all_refs:
        ref_counts[ref_info["ref"]] += 1

    # Sort by frequency
    most_cited = sorted(ref_counts.items(), key=lambda x: -x[1])

    # Classify by canon
    by_canon = defaultdict(list)
    for ref in unique_refs:
        canon = classify_canon(ref)
        by_canon[canon].append(ref)

    # Section coverage
    section_coverage = {}
    for section, refs in refs_by_section.items():
        section_coverage[section] = {
            "count": len(refs),
            "unique": len(set(refs)),
            "refs": list(set(refs)),
        }

    # Load backlinks for cross-site analysis
    backlinks = load_backlinks()
    current_url_prefix = f"/weeks/{week_num}/" if week_num else None

    cross_site_reuse = {}
    unique_to_week = []

    for ref in unique_refs:
        if ref in backlinks:
            other_locations = []
            for occ in backlinks[ref]:
                # Skip current week's own entries
                if current_url_prefix and occ["url"].startswith(current_url_prefix):
                    continue
                other_locations.append({
                    "title": occ["title"],
                    "url": occ["url"],
                    "section": occ.get("section"),
                })
            if other_locations:
                cross_site_reuse[ref] = other_locations
            else:
                unique_to_week.append(ref)
        else:
            unique_to_week.append(ref)

    # Load expected passages
    expected_passages = load_expected_passages()
    week_key = f"week{week_num}" if week_num else None
    expected = expected_passages.get(week_key, [])

    expected_status = {}
    for passage in expected:
        # Check if any ref matches or contains this passage
        found_count = 0
        for ref in unique_refs:
            if passage in ref or ref in passage or passage == ref:
                found_count += ref_counts.get(ref, 0)
        if found_count == 0:
            expected_status[passage] = "missing"
        elif found_count == 1:
            expected_status[passage] = "present"
        elif found_count <= 3:
            expected_status[passage] = "present"
        else:
            expected_status[passage] = "heavy"

    # Theme concentration warnings
    warnings = []

    # Check for sections with no scripture
    for section, data in section_coverage.items():
        if data["count"] == 0:
            warnings.append(f"'{section}' has no scripture references")
        elif data["count"] == 1:
            warnings.append(f"'{section}' has very light scripture coverage (1 ref)")

    # Check for over-concentration
    if most_cited and most_cited[0][1] >= 5:
        ref, count = most_cited[0]
        warnings.append(f"{ref} is heavily concentrated ({count} citations)")

    # Check chapter imbalance
    chapter_counts = defaultdict(int)
    for ref in all_refs:
        chapter = extract_chapter(ref["ref"])
        chapter_counts[chapter] += 1

    if len(chapter_counts) >= 2:
        sorted_chapters = sorted(chapter_counts.items(), key=lambda x: -x[1])
        top_chapter, top_count = sorted_chapters[0]
        if top_count > total_citations * 0.5 and total_citations >= 6:
            warnings.append(f"{top_chapter} dominates citations ({top_count}/{total_citations})")

    return {
        "week": week_num,
        "files_analyzed": [f.name for f in files],
        "unique_refs": len(unique_refs),
        "total_citations": total_citations,
        "most_cited": most_cited[:10],
        "by_canon": {k: sorted(v) for k, v in by_canon.items()},
        "section_coverage": section_coverage,
        "expected_status": expected_status,
        "cross_site_reuse": cross_site_reuse,
        "unique_to_week": sorted(unique_to_week),
        "warnings": warnings,
    }


def generate_markdown_report(analysis: dict) -> str:
    """Generate a markdown report from analysis."""
    lines = []
    week = analysis.get("week", "Unknown")

    lines.append(f"# Scripture Usage Radar — Week {week}")
    lines.append("")
    lines.append(f"*Files analyzed: {', '.join(analysis.get('files_analyzed', []))}*")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append(f"- **Unique references:** {analysis['unique_refs']}")
    lines.append(f"- **Total citations:** {analysis['total_citations']}")

    if analysis['most_cited']:
        top_refs = ", ".join(f"{ref} ({count})" for ref, count in analysis['most_cited'][:5])
        lines.append(f"- **Most cited:** {top_refs}")
    lines.append("")

    # By Canon
    lines.append("## References by Canon")
    for canon in ["OT", "NT", "BoM", "D&C", "PGP", "Other"]:
        refs = analysis['by_canon'].get(canon, [])
        if refs:
            lines.append(f"- **{canon}:** {len(refs)} refs")
    lines.append("")

    # Section Coverage
    lines.append("## Section Coverage")
    for section, data in sorted(analysis['section_coverage'].items()):
        count = data['count']
        unique = data['unique']
        if count == 0:
            status = "⚠️"
        elif count <= 2:
            status = "○"
        else:
            status = "●"
        lines.append(f"- {status} **{section}:** {count} citations ({unique} unique)")
    lines.append("")

    # Expected Anchor Passages
    if analysis['expected_status']:
        lines.append("## Expected Anchor Passages")
        for passage, status in analysis['expected_status'].items():
            if status == "missing":
                icon = "❌"
            elif status == "heavy":
                icon = "🔥"
            else:
                icon = "✓"
            lines.append(f"- {icon} {passage} — {status}")
        lines.append("")

    # Cross-Site Reuse
    if analysis['cross_site_reuse']:
        lines.append("## Cross-Site Reuse")
        lines.append("*References that also appear elsewhere on the site:*")
        lines.append("")
        for ref, locations in sorted(analysis['cross_site_reuse'].items()):
            lines.append(f"### {ref}")
            for loc in locations[:3]:  # Limit to 3 locations
                section_note = f" ({loc['section']})" if loc.get('section') else ""
                lines.append(f"- [{loc['title']}]({loc['url']}){section_note}")
            if len(locations) > 3:
                lines.append(f"- *...and {len(locations) - 3} more*")
            lines.append("")

    # Unique to This Week
    if analysis['unique_to_week']:
        lines.append("## Unique to This Week")
        lines.append(f"*{len(analysis['unique_to_week'])} references not found elsewhere on the site:*")
        lines.append("")
        # Group by book for readability
        by_book = defaultdict(list)
        for ref in analysis['unique_to_week']:
            book = extract_book(ref)
            by_book[book].append(ref)
        for book in sorted(by_book.keys()):
            refs = by_book[book]
            lines.append(f"- **{book}:** {', '.join(refs)}")
        lines.append("")

    # Warnings
    if analysis['warnings']:
        lines.append("## Warnings")
        for warning in analysis['warnings']:
            lines.append(f"- ⚠️ {warning}")
        lines.append("")

    lines.append("---")
    lines.append("*Generated by scripture-usage-radar.py*")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Scripture Usage Radar - Editorial QA Reports')
    parser.add_argument('--week', '-w', type=int, help='Week number to analyze')
    parser.add_argument('--path', '-p', type=str, help='Path to content directory or file')
    parser.add_argument('--output', '-o', type=str, help='Output file path (default: reports/weekN_radar.md)')
    parser.add_argument('--json', action='store_true', help='Also output JSON analysis')
    parser.add_argument('--quiet', '-q', action='store_true', help='Suppress console output')

    args = parser.parse_args()

    if not args.week and not args.path:
        print("Error: Must specify --week or --path", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    if args.week:
        analysis = analyze_week(args.week)
    else:
        path = Path(args.path)
        if not path.exists():
            print(f"Error: Path not found: {path}", file=sys.stderr)
            sys.exit(1)
        # Try to extract week number from path
        week_match = re.search(r'week(\d+)', str(path))
        week_num = int(week_match.group(1)) if week_match else None
        analysis = analyze_path(path, week_num)

    if "error" in analysis:
        print(f"Error: {analysis['error']}", file=sys.stderr)
        sys.exit(1)

    # Generate report
    report = generate_markdown_report(analysis)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        week_str = f"week{analysis['week']}" if analysis.get('week') else "analysis"
        output_path = REPORTS_DIR / f"{week_str}_scripture_radar.md"

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding='utf-8')

    if not args.quiet:
        print(f"Report written to: {output_path}")
        print("")
        print(report)

    # Write JSON if requested
    if args.json:
        json_path = output_path.with_suffix('.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        if not args.quiet:
            print(f"\nJSON written to: {json_path}")


if __name__ == '__main__':
    main()
