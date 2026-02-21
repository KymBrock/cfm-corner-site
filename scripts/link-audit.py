#!/usr/bin/env python3
"""
CFM Corner Link Audit Script
Scans all insights.html files for unlinked Hebrew terms, scripture references,
and bare transliterations that should have BLB popup links.

Usage:  python3 scripts/link-audit.py
        python3 scripts/link-audit.py --week week09
        python3 scripts/link-audit.py --fix-scriptures   (auto-links bare scripture refs)
"""

import re, glob, json, sys, os

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Book name → BLB abbreviation + display name ──────────────────────────────
BOOK_BLB = {
    'genesis':'gen','exodus':'exo','leviticus':'lev','numbers':'num',
    'deuteronomy':'deu','joshua':'jos','judges':'jdg','ruth':'rut',
    '1 samuel':'1sa','2 samuel':'2sa','1 kings':'1ki','2 kings':'2ki',
    '1 chronicles':'1ch','2 chronicles':'2ch','ezra':'ezr','nehemiah':'neh',
    'esther':'est','job':'job','psalms':'psa','psalm':'psa','proverbs':'pro',
    'ecclesiastes':'ecc','isaiah':'isa','jeremiah':'jer','lamentations':'lam',
    'ezekiel':'eze','daniel':'dan','hosea':'hos','joel':'joe','amos':'amo',
    'obadiah':'oba','jonah':'jon','micah':'mic','nahum':'nah','habakkuk':'hab',
    'zephaniah':'zep','haggai':'hag','zechariah':'zec','malachi':'mal',
    'matthew':'mat','mark':'mar','luke':'luk','john':'jhn','acts':'act',
    'romans':'rom','1 corinthians':'1co','2 corinthians':'2co',
    'galatians':'gal','ephesians':'eph','philippians':'phi','colossians':'col',
    '1 thessalonians':'1th','2 thessalonians':'2th','1 timothy':'1ti',
    '2 timothy':'2ti','titus':'tit','philemon':'phm','hebrews':'heb',
    'james':'jam','1 peter':'1pe','2 peter':'2pe','1 john':'1jo',
    '2 john':'2jn','3 john':'3jn','jude':'jde','revelation':'rev',
}

# Short abbreviations used inline (Gen., Matt., etc.) → full name
ABBR_MAP = {
    'gen':'genesis','exo':'exodus','lev':'leviticus','num':'numbers',
    'deu':'deuteronomy','deut':'deuteronomy','jos':'joshua','jdg':'judges',
    '1sa':'1 samuel','2sa':'2 samuel','1ki':'1 kings','2ki':'2 kings',
    '1ch':'1 chronicles','2ch':'2 chronicles','neh':'nehemiah','est':'esther',
    'job':'job','psa':'psalms','ps':'psalms','pro':'proverbs','prov':'proverbs',
    'ecc':'ecclesiastes','eccl':'ecclesiastes','isa':'isaiah','jer':'jeremiah',
    'lam':'lamentations','eze':'ezekiel','ezek':'ezekiel','dan':'daniel',
    'hos':'hosea','amo':'amos','mic':'micah','nah':'nahum','hab':'habakkuk',
    'zep':'zephaniah','hag':'haggai','zec':'zechariah','zech':'zechariah',
    'mal':'malachi','mat':'matthew','matt':'matthew','mar':'mark','mrk':'mark',
    'luk':'luke','jhn':'john','act':'acts','rom':'romans',
    '1co':'1 corinthians','1cor':'1 corinthians',
    '2co':'2 corinthians','2cor':'2 corinthians',
    'gal':'galatians','eph':'ephesians','phi':'philippians','php':'philippians',
    'col':'colossians','heb':'hebrews','jam':'james','jas':'james',
    '1pe':'1 peter','1pet':'1 peter','2pe':'2 peter','2pet':'2 peter',
    '1jo':'1 john','1jn':'1 john','jde':'jude','jud':'jude','rev':'revelation',
}

BOOK_ABBRS_RE = (
    r'(?:1|2|3\s)?(?:'
    r'Gen(?:esis)?|Exo(?:d(?:us)?)?|Lev(?:iticus)?|Num(?:bers)?'
    r'|Deu(?:t(?:eronomy)?)?|Jos(?:hua)?|Jud(?:g(?:es)?)?|Ruth'
    r'|[12]\s*Sam(?:uel)?|[12]\s*Ki(?:ngs?)?|[12]\s*Chr(?:on(?:icles)?)?'
    r'|Ezr(?:a)?|Neh(?:emiah)?|Est(?:her)?|Job|Ps(?:a(?:lms?)?)?'
    r'|Pro(?:v(?:erbs?)?)?|Ecc(?:l(?:esiastes)?)?'
    r'|Isa(?:iah)?|Jer(?:emiah)?|Lam(?:entations)?|Eze(?:k(?:iel)?)?'
    r'|Dan(?:iel)?|Hos(?:ea)?|Joel?|Amos?|Mic(?:ah)?|Nah(?:um)?'
    r'|Hab(?:akkuk)?|Zep(?:haniah)?|Hag(?:gai)?|Zec(?:h(?:ariah)?)?|Mal(?:achi)?'
    r'|Matt?(?:hew)?|Mar(?:k)?|Luk(?:e)?|John?|Act(?:s)?|Rom(?:ans?)?'
    r'|[12]\s*Cor(?:inthians?)?|Gal(?:atians?)?|Eph(?:esians?)?'
    r'|Phil(?:ippians?)?|Col(?:ossians?)?|Heb(?:rews?)?|Jas?(?:mes?)?'
    r'|[12]\s*Pet(?:er)?|[123]\s*John?|Jude?|Rev(?:elation)?'
    r')'
)

BARE_SCRIPTURE_RE = re.compile(
    rf'\((?:{BOOK_ABBRS_RE})[.\s]*\d+(?:[:\-]\d+)+(?:[,\s–—-]\d+)*\)'
    r'|\(\d{1,3}:\d{1,3}(?:[–,\s]\d+)?\)',
    re.IGNORECASE
)

DOUBLE_LINK_RE = re.compile(r'\[\[([^\]]+)\]\(([^)]+)\)\]\([^)]+\)')

def load_lexicon():
    path = f'{SITE_ROOT}/static/data/lexicon-popups.json'
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def get_known_translits(lexicon):
    translits = set()
    for v in lexicon.values():
        t = v.get('translit', '')
        if t:
            translits.add(t.lower().replace("'", "'"))
    return translits

def audit_file(fpath, known_translits):
    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    # Strip linked content
    stripped = re.sub(r'<a [^>]+>.*?</a>', '[[LINKED]]', content, flags=re.DOTALL)

    issues = []

    # 1. Bare Hebrew characters (Unicode block)
    for m in re.finditer(r'[\u05b0-\u05ea\ufb1d-\ufb4e]{2,}', stripped):
        context = stripped[max(0, m.start()-40):m.end()+40].replace('\n', ' ').strip()
        issues.append(('BARE HEBREW', m.group(), context))

    # 2. Bare scripture references
    for m in BARE_SCRIPTURE_RE.finditer(stripped):
        context = stripped[max(0, m.start()-50):m.end()+50].replace('\n', ' ').strip()
        issues.append(('BARE SCRIPTURE', m.group(), context))

    # 3. Bare <em> with known Hebrew transliterations
    for m in re.finditer(r'<em>([^<]{2,35})</em>', stripped):
        term = m.group(1).strip().lower().replace("'", "'")
        if term in known_translits:
            context = stripped[max(0, m.start()-40):m.end()+40].replace('\n', ' ').strip()
            issues.append(('BARE TRANSLIT', m.group(1), context))

    # 4. Double-nested markdown links (for .md files)
    for m in DOUBLE_LINK_RE.finditer(content):
        issues.append(('DOUBLE LINK', m.group(), ''))

    return issues

def main():
    args = sys.argv[1:]
    week_filter = None
    if '--week' in args:
        idx = args.index('--week')
        week_filter = args[idx + 1]

    lexicon = load_lexicon()
    known_translits = get_known_translits(lexicon)

    pattern = f'{SITE_ROOT}/static/content/**/insights.html'
    if week_filter:
        pattern = f'{SITE_ROOT}/static/content/{week_filter}/insights.html'

    files = sorted(glob.glob(pattern, recursive=True))
    if not files:
        print(f"No files found matching: {pattern}")
        return

    total_issues = 0
    weeks_with_issues = 0

    for fpath in files:
        week = fpath.split('/')[-2]
        issues = audit_file(fpath, known_translits)
        if issues:
            weeks_with_issues += 1
            print(f'\n{"="*60}')
            print(f'  {week}  ({len(issues)} issues)')
            print(f'{"="*60}')
            for kind, term, ctx in issues:
                print(f'\n  [{kind}]  "{term}"')
                if ctx:
                    print(f'  ...{ctx[:120]}...')
            total_issues += len(issues)

    print(f'\n{"="*60}')
    print(f'TOTAL: {total_issues} issues across {weeks_with_issues} weeks')
    print(f'{"="*60}')

    if total_issues == 0:
        print('\n✅ All clear — no unlinked terms found.')

if __name__ == '__main__':
    main()
