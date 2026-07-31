#!/usr/bin/env python3
"""
Link bare <em>transliteration</em> terms in the culture guides using the
ESTABLISHED, collision-safe system: HugoConverter._auto_link_transliterations
(cfm-corner-tools), which is backed by lexicon-popups.json + translit-aliases.json
and puts the link on the transliteration (keeping Hebrew/Greek script bare so
niqqud stays unobstructed).

Frontmatter is never touched. Usage:
  python3 scripts/culture-translit-linker.py --guide babylon [--write]
  python3 scripts/culture-translit-linker.py --guide '*' --write
"""
import sys, os, re, glob, argparse, importlib.util

FM = re.compile(r'^(---\n.*?\n---\n)', re.DOTALL)

# False positives from <em>-overload in the culture guides (emphasis/place-names, not
# transliterations). Reviewed & approved for blocking; unwrap them from the linker output.
BLOCK = ['Babylon', 'Tel Aviv', 'idea', 'reach', 'Peleset', 'Shekelesh', 'Sariah']
BLOCK_RE = re.compile(
    r'<a\b[^>]*lexicon[^>]*>\s*<em>(' + '|'.join(re.escape(b) for b in BLOCK) + r')</em>\s*</a>',
    re.IGNORECASE)

def apply_blocklist(html):
    return BLOCK_RE.sub(r'<em>\1</em>', html)

def fix_alt_strongs(html):
    """The aliases file disambiguates homonyms with an internal `_ALT_<script>` marker
    (e.g. mishkan -> H4908_ALT_מִש). BLB URLs need only the base Strong's number, so
    strip the marker from the href and data-strongs so the link resolves."""
    html = re.sub(r'(lexicon/[hg]\d+)_alt_[^/"]*', r'\1', html)
    html = re.sub(r'(data-strongs="[HG]\d+)_ALT_[^"]*"', r'\1"', html)
    return html

def get_conv():
    spec = importlib.util.spec_from_file_location('la', os.path.join(os.path.dirname(__file__), 'link-audit.py'))
    la = importlib.util.module_from_spec(spec); spec.loader.exec_module(la)
    return la._get_converter()

def count_lexlinks(s):
    return len(re.findall(r'href="https://www\.blueletterbible\.org/lexicon/', s))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--guide', default='*')
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    conv = get_conv()
    assert conv is not None, "HugoConverter not available"
    if a.guide == '*':
        files = sorted(glob.glob('content/culture/ancient/*/*.md'))
    else:
        files = sorted(glob.glob(f'content/culture/ancient/{a.guide}/*.md'))
    grand = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        m = FM.match(s); fm = m.group(1) if m else ''; body = s[m.end():] if m else s
        before = count_lexlinks(body)
        new_body = fix_alt_strongs(apply_blocklist(conv._auto_link_transliterations(body)))
        added = count_lexlinks(new_body) - before
        # safety: tag balance must be preserved
        if new_body.count('<a ') != new_body.count('</a>'):
            print(f"  !! UNBALANCED after transform, SKIP {f}"); continue
        if added:
            grand += added
            print(f"{added:4}  {f}")
            if a.write:
                open(f, 'w', encoding='utf-8').write(fm + new_body)
    print(f"\n{'WROTE' if a.write else 'DRY-RUN'} total translit links added: {grand}")

if __name__ == '__main__':
    main()
