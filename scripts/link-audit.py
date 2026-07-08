#!/usr/bin/env python3
"""
CFM Corner Link Audit Script
Scans study-guide.html, insights.html, AND resources.html files for unlinked
Hebrew terms (including dash-separated roots), scripture references, bare
transliterations, BLB lexicon links missing popup data attributes, and
word studies missing Cross-Language Connections tables.

Usage:  python3 scripts/link-audit.py
        python3 scripts/link-audit.py --week week10
        python3 scripts/link-audit.py --type study-guide     (study-guide.html only)
        python3 scripts/link-audit.py --type insights         (insights.html only)
        python3 scripts/link-audit.py --type resources        (resources.html only)
        python3 scripts/link-audit.py --fix                   (auto-link all bare terms in-place)
        python3 scripts/link-audit.py --fix --week week10     (auto-link only week10)
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
            translits.add(t.lower().replace("'", "\u2019"))
    return translits

def audit_file(fpath, known_translits):
    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    # Strip linked content and button headings (Hebrew in <button> is expected)
    stripped = re.sub(r'<a [^>]+>.*?</a>', '[[LINKED]]', content, flags=re.DOTALL)
    stripped = re.sub(r'<button[^>]*>.*?</button>', '[[BUTTON]]', stripped, flags=re.DOTALL)

    issues = []

    # 1a. Bare Hebrew characters (Unicode block — contiguous runs)
    for m in re.finditer(r'[\u05b0-\u05ea\ufb1d-\ufb4e]{2,}', stripped):
        context = stripped[max(0, m.start()-40):m.end()+40].replace('\n', ' ').strip()
        issues.append(('BARE HEBREW', m.group(), context))

    # 1b. Bare Hebrew root consonants (dash-separated, e.g., ב-ר-כ)
    for m in re.finditer(r'[\u05d0-\u05ea](?:\s*[-\u2010-\u2015]\s*[\u05d0-\u05ea]){1,4}', stripped):
        context = stripped[max(0, m.start()-40):m.end()+40].replace('\n', ' ').strip()
        issues.append(('BARE ROOT', m.group(), context))

    # 2. Bare scripture references
    for m in BARE_SCRIPTURE_RE.finditer(stripped):
        context = stripped[max(0, m.start()-50):m.end()+50].replace('\n', ' ').strip()
        issues.append(('BARE SCRIPTURE', m.group(), context))

    # 3. Bare <em> with known Hebrew transliterations
    for m in re.finditer(r'<em>([^<]{2,35})</em>', stripped):
        term = m.group(1).strip().lower().replace("'", "\u2019")
        if term in known_translits:
            context = stripped[max(0, m.start()-40):m.end()+40].replace('\n', ' ').strip()
            issues.append(('BARE TRANSLIT', m.group(1), context))

    # 4. BLB lexicon links missing data-lexicon attribute
    for m in re.finditer(r'<a [^>]*href="[^"]*blueletterbible\.org/lexicon/[^"]*"[^>]*>.*?</a>', content, flags=re.DOTALL):
        tag = m.group()
        if 'data-lexicon' not in tag:
            url_m = re.search(r'href="([^"]+)"', tag)
            url = url_m.group(1) if url_m else '?'
            inner = re.sub(r'<[^>]+>', '', tag).strip()
            issues.append(('BARE BLB LINK', f'{inner} → {url}', ''))

    # 5. Double-nested markdown links (for .md files)
    for m in DOUBLE_LINK_RE.finditer(content):
        issues.append(('DOUBLE LINK', m.group(), ''))

    # 6. Missing Cross-Language Connections tables (study-guide.html only)
    if fpath.endswith('study-guide.html'):
        issues.extend(_check_cross_language_tables(content))

    return issues


def _check_cross_language_tables(content):
    """Check that every Word Study in a study-guide.html has a Cross-Language Connections table."""
    issues = []

    # Find all word study sub-accordion buttons
    # Pattern: <button class="sg-sub-accordion"><span>Word Study N: Title</span></button>
    ws_buttons = list(re.finditer(
        r'<button[^>]*class="sg-sub-accordion"[^>]*>\s*<span>\s*(Word Study \d+:[^<]*)</span>',
        content, re.IGNORECASE
    ))

    if not ws_buttons:
        return issues  # No word studies in this file (not an error)

    for i, btn_match in enumerate(ws_buttons):
        ws_title = btn_match.group(1).strip()
        start_pos = btn_match.end()

        # End position = next word study button or end of content
        if i + 1 < len(ws_buttons):
            end_pos = ws_buttons[i + 1].start()
        else:
            end_pos = len(content)

        section = content[start_pos:end_pos]

        # Check for Cross-Language Connections heading
        has_heading = bool(re.search(
            r'<h3>\s*Cross-Language Connections\s*</h3>', section, re.IGNORECASE
        ))

        if not has_heading:
            issues.append(('MISSING CROSS-LANG', ws_title, 'No <h3>Cross-Language Connections</h3> found'))
            continue

        # Verify the table has key components
        has_table = '<table' in section.split('Cross-Language Connections')[1] if 'Cross-Language Connections' in section else False

        if not has_table:
            issues.append(('MISSING CROSS-LANG', ws_title, 'Has heading but no <table> follows'))
            continue

        # Extract the cross-language section (from heading to next <hr> or end)
        cl_start = section.index('Cross-Language Connections')
        cl_section = section[cl_start:]
        # Trim to the table area (up to next <hr> or next <h2>/<h3> that isn't part of this)
        hr_match = re.search(r'</table>', cl_section)
        if hr_match:
            cl_section = cl_section[:hr_match.end()]

        # Check for Greek (LXX) row with BLB link
        has_greek = bool(re.search(r'Greek\s*\(LXX\)', cl_section))
        if not has_greek:
            issues.append(('MISSING CROSS-LANG', ws_title, 'Table missing Greek (LXX) row'))

        # Check for Latin (Vulgate) row with Logeion link
        has_latin = bool(re.search(r'logeion\.uchicago\.edu', cl_section))
        if not has_latin:
            issues.append(('MISSING CROSS-LANG', ws_title, 'Table missing Latin row (no Logeion link)'))

        # Check for English row with MW + 1828 links
        has_1828 = bool(re.search(r'webstersdictionary1828\.com', cl_section))
        has_mw = bool(re.search(r'merriam-webster\.com', cl_section))
        if not has_mw or not has_1828:
            missing = []
            if not has_mw:
                missing.append('Merriam-Webster')
            if not has_1828:
                missing.append("Webster's 1828")
            issues.append(('MISSING CROSS-LANG', ws_title, f'Table missing English links: {", ".join(missing)}'))

    return issues


def main():
    args = sys.argv[1:]
    week_filter = None
    type_filter = None  # None = all three file types
    fix_mode = '--fix' in args

    if '--week' in args:
        idx = args.index('--week')
        week_filter = args[idx + 1]
    if '--type' in args:
        idx = args.index('--type')
        type_filter = args[idx + 1]

    lexicon = load_lexicon()
    known_translits = get_known_translits(lexicon)

    # ── Determine which HTML files to scan ──
    file_types = []
    if type_filter == 'study-guide':
        file_types = ['study-guide.html']
    elif type_filter == 'insights':
        file_types = ['insights.html']
    elif type_filter == 'resources':
        file_types = ['resources.html']
    else:
        file_types = ['study-guide.html', 'insights.html', 'resources.html']

    files = []
    for ft in file_types:
        if week_filter:
            pattern = f'{SITE_ROOT}/static/content/{week_filter}/{ft}'
        else:
            pattern = f'{SITE_ROOT}/static/content/**/{ft}'
        files.extend(glob.glob(pattern, recursive=True))

    files = sorted(files)
    if not files:
        print(f"No files found. Searched for: {', '.join(file_types)}")
        return

    print(f'Scanning {len(files)} files ({", ".join(file_types)})...\n')

    total_issues = 0
    files_with_issues = 0

    for fpath in files:
        week = fpath.split('/')[-2]
        fname = os.path.basename(fpath)
        label = f'{week}/{fname}'
        issues = audit_file(fpath, known_translits)
        if issues:
            files_with_issues += 1
            print(f'\n{"="*60}')
            print(f'  {label}  ({len(issues)} issues)')
            print(f'{"="*60}')
            for kind, term, ctx in issues:
                print(f'\n  [{kind}]  "{term}"')
                if ctx:
                    print(f'  ...{ctx[:120]}...')
            total_issues += len(issues)

    print(f'\n{"="*60}')
    print(f'TOTAL: {total_issues} issues across {files_with_issues} files')
    print(f'{"="*60}')

    if total_issues == 0:
        print('\n✅ All clear — no unlinked terms found.')
        return

    # ── --fix mode: auto-link bare terms in-place ──────────────────────────────
    if fix_mode:
        print('\n🔧 FIX MODE: applying auto-linkers to files with issues...\n')
        converter = _get_converter()
        if converter is None:
            print('  ❌ Could not load HugoConverter — fix mode unavailable.')
            return

        fixed_files = 0
        for fpath in files:
            issues = audit_file(fpath, known_translits)
            if not issues:
                continue

            with open(fpath, encoding='utf-8') as f:
                original = f.read()

            html = original
            html = converter._auto_link_scriptures(html)
            html = converter._auto_link_hebrew_greek(html)
            if hasattr(converter, '_auto_link_transliterations'):
                html = converter._auto_link_transliterations(html)

            if html != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(html)
                week = fpath.split('/')[-2]
                fname = os.path.basename(fpath)
                print(f'  ✅ Fixed {week}/{fname}')
                fixed_files += 1

        print(f'\n  Fixed {fixed_files} file(s).')

        # Re-audit to show remaining issues
        print('\n── Re-auditing after fix ──\n')
        remaining = 0
        for fpath in files:
            issues = audit_file(fpath, known_translits)
            if issues:
                week = fpath.split('/')[-2]
                fname = os.path.basename(fpath)
                print(f'  {week}/{fname}: {len(issues)} remaining issues')
                for kind, term, ctx in issues:
                    print(f'    [{kind}]  "{term}"')
                remaining += len(issues)
        if remaining == 0:
            print('  ✅ All clear after fix — zero issues remain.')
        else:
            print(f'\n  ⚠️  {remaining} issues remain (may need manual attention).')


def _get_converter():
    """Import and instantiate HugoConverter from cfm-corner-tools."""
    tools_root = os.path.join(os.path.dirname(SITE_ROOT), 'cfm-corner-tools')
    converter_path = os.path.join(tools_root, 'converters', 'hugo_converter.py')
    if not os.path.exists(converter_path):
        print(f'  ⚠️  HugoConverter not found at {converter_path}')
        return None
    try:
        sys.path.insert(0, os.path.join(tools_root, 'converters'))
        from hugo_converter import HugoConverter
        return HugoConverter()
    except Exception as e:
        print(f'  ⚠️  Failed to load HugoConverter: {e}')
        return None


if __name__ == '__main__':
    main()
