#!/usr/bin/env python3
"""
Scripture Citation Back-Link Builder

Scans generated HTML for data-ref attributes and builds an index of where
each scripture reference appears across the site.

Usage:
    python scripts/build-scripture-backlinks.py
    python scripts/build-scripture-backlinks.py --output static/data/scripture-backlinks.json

Output: JSON index mapping canonical refs to their occurrences across the site.
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
OUTPUT_PATH = Path(__file__).parent.parent / "static" / "data" / "scripture-backlinks.json"

# Content type display names
CONTENT_TYPE_NAMES = {
    "study-guide": "Study Guide",
    "insights": "Insights",
    "resources": "Resources",
    "culture": "Culture",
    "comparison": "Comparison",
    "hebrew": "Hebrew",
}


class ScriptureRefExtractor(HTMLParser):
    """HTML parser that extracts data-ref attributes and section context."""

    def __init__(self):
        super().__init__()
        self.refs = []  # List of (ref, section, excerpt)
        self.current_section = None
        self.in_section_header = False
        self.section_header_depth = 0
        self.current_excerpt = []
        self.capture_excerpt = False
        self.excerpt_chars = 0
        self.max_excerpt_chars = 80

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Track section headers
        if tag == "div" and "section-header" in attrs_dict.get("class", ""):
            self.in_section_header = True
            self.section_header_depth = 1
        elif self.in_section_header and tag == "div":
            self.section_header_depth += 1

        # Extract data-ref
        if "data-ref" in attrs_dict:
            ref = attrs_dict["data-ref"]
            if ref:
                normalized = normalize_ref(ref)
                self.refs.append({
                    "ref": normalized,
                    "section": self.current_section,
                    "excerpt": None  # Could capture surrounding text
                })

    def handle_endtag(self, tag):
        if self.in_section_header and tag == "div":
            self.section_header_depth -= 1
            if self.section_header_depth == 0:
                self.in_section_header = False

    def handle_data(self, data):
        # Capture section header text
        if self.in_section_header:
            text = data.strip()
            # Skip button labels and arrows
            if text and text not in ["⊞", "⊟", "▶︎", "▼", "◀", "▲"]:
                self.current_section = text


def normalize_ref(ref: str) -> str:
    """
    Normalize a scripture reference to canonical form.

    - Strip whitespace
    - Normalize dash variants (–, —, −) to hyphen (-)
    - Normalize spaces around dashes
    - Handle "Genesis 1:1 - 3" → "Genesis 1:1-3"
    """
    ref = ref.strip()

    # Replace various dash characters with hyphen
    ref = re.sub(r'[–—−]', '-', ref)

    # Normalize "1:1 - 3" to "1:1-3"
    ref = re.sub(r'\s*-\s*', '-', ref)

    # Normalize multiple spaces
    ref = re.sub(r'\s+', ' ', ref)

    return ref


def file_to_url(filepath: Path, content_dir: Path) -> str:
    """
    Map a file path to its public URL.

    static/content/week11/study-guide.html → /weeks/11/study-guide/
    static/content/week11/insights.html → /weeks/11/insights/
    """
    rel_path = filepath.relative_to(content_dir)
    parts = rel_path.parts

    if len(parts) >= 2:
        week_dir = parts[0]  # e.g., "week11"
        content_file = parts[1]  # e.g., "study-guide.html"

        # Extract week number
        week_match = re.match(r'week(\d+)', week_dir)
        if week_match:
            week_num = int(week_match.group(1))
            content_type = content_file.replace('.html', '')
            return f"/weeks/{week_num}/{content_type}/"

    # Fallback: use relative path
    return "/" + str(rel_path).replace('.html', '/').replace('\\', '/')


def get_page_title(filepath: Path) -> str:
    """
    Generate a page title from the file path.

    week11/study-guide.html → "Week 11 Study Guide"
    """
    rel_path = filepath.relative_to(CONTENT_DIR)
    parts = rel_path.parts

    if len(parts) >= 2:
        week_dir = parts[0]
        content_file = parts[1].replace('.html', '')

        week_match = re.match(r'week(\d+)', week_dir)
        if week_match:
            week_num = int(week_match.group(1))
            content_name = CONTENT_TYPE_NAMES.get(content_file, content_file.replace('-', ' ').title())
            return f"Week {week_num} {content_name}"

    return filepath.stem.replace('-', ' ').title()


def get_content_type(filepath: Path) -> str:
    """Extract content type from filename."""
    return filepath.stem  # study-guide, insights, etc.


def extract_refs_from_file(filepath: Path) -> list:
    """
    Extract all data-ref attributes from an HTML file.

    Returns list of dicts with ref, section, excerpt.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        parser = ScriptureRefExtractor()
        parser.feed(content)
        return parser.refs
    except Exception as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return []


def build_backlinks(content_dir: Path) -> dict:
    """
    Build the complete back-link index.

    Returns dict mapping canonical refs to list of occurrences.
    """
    # Collect all occurrences
    all_occurrences = defaultdict(list)

    # Scan all HTML files
    html_files = list(content_dir.rglob("*.html"))

    for filepath in html_files:
        refs = extract_refs_from_file(filepath)

        if not refs:
            continue

        url = file_to_url(filepath, content_dir)
        title = get_page_title(filepath)
        content_type = get_content_type(filepath)

        # Group by (ref, section) to count occurrences
        section_counts = defaultdict(int)
        for ref_info in refs:
            key = (ref_info["ref"], ref_info["section"])
            section_counts[key] += 1

        # Add deduplicated entries
        for (ref, section), count in section_counts.items():
            all_occurrences[ref].append({
                "url": url,
                "title": title,
                "content_type": content_type,
                "section": section,
                "count": count
            })

    # Sort by ref and then by url within each ref
    sorted_index = {}
    for ref in sorted(all_occurrences.keys()):
        occurrences = all_occurrences[ref]
        # Sort by URL for consistent output
        occurrences.sort(key=lambda x: (x["url"], x["section"] or ""))
        sorted_index[ref] = occurrences

    return sorted_index


def print_summary(index: dict):
    """Print a summary of the back-link index."""
    total_refs = len(index)
    total_occurrences = sum(len(occs) for occs in index.values())

    # Find most-cited refs
    ref_counts = [(ref, sum(o["count"] for o in occs)) for ref, occs in index.items()]
    ref_counts.sort(key=lambda x: -x[1])

    print("\n" + "=" * 60)
    print("SCRIPTURE BACK-LINK INDEX SUMMARY")
    print("=" * 60)
    print(f"\nUnique references indexed: {total_refs}")
    print(f"Total page/section entries: {total_occurrences}")

    print("\n" + "-" * 60)
    print("Most-cited references (top 15):")
    print("-" * 60)
    for ref, count in ref_counts[:15]:
        pages = len(index[ref])
        print(f"  {ref}: {count} citations across {pages} page(s)")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description='Build scripture citation back-link index')
    parser.add_argument('--content', '-c', default=str(CONTENT_DIR),
                        help='Path to content directory')
    parser.add_argument('--output', '-o', default=str(OUTPUT_PATH),
                        help='Output JSON path')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Suppress summary output')

    args = parser.parse_args()

    content_dir = Path(args.content)
    output_path = Path(args.output)

    if not content_dir.exists():
        print(f"Error: Content directory not found: {content_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning {content_dir}...")
    index = build_backlinks(content_dir)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Wrote {output_path}")

    if not args.quiet:
        print_summary(index)


if __name__ == '__main__':
    main()
