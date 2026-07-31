#!/usr/bin/env python3
"""
Culture-guide scripture auto-linker.

Wraps BARE (unlinked) scripture references in the culture field guides with the
same anchor format the guides already use:
  biblical -> BLB:    <a href="https://www.blueletterbible.org/kjv/{abbr}/{ch}/{v}/" target="_blank" data-ref="Book Ch:V">TEXT</a>
  LDS      -> Church:  <a href="https://www.churchofjesuschrist.org/study/scriptures/{vol}/{slug}/{ch}?lang=eng&id={v}" target="_blank" data-ref="Book Ch:V">TEXT</a>

SAFETY: it tokenizes the HTML and only linkifies inside TEXT nodes that are NOT
inside <a>...</a> and NOT inside <script>...</script>. It never edits tag
attributes (data-caption, href, data-ref, etc.) because those live inside tag
tokens, which are passed through untouched. Idempotent.

Usage:
  python3 scripts/culture-scripture-linker.py --dry-run [--guide babylon] [--set biblical|lds|all]
  python3 scripts/culture-scripture-linker.py --write   --guide babylon --set biblical
"""
import re, glob, sys, os, argparse

BOOK_BLB = {
 'genesis':'gen','exodus':'exo','leviticus':'lev','numbers':'num','deuteronomy':'deu',
 'joshua':'jos','judges':'jdg','ruth':'rut','1 samuel':'1sa','2 samuel':'2sa',
 '1 kings':'1ki','2 kings':'2ki','1 chronicles':'1ch','2 chronicles':'2ch','ezra':'ezr',
 'nehemiah':'neh','esther':'est','job':'job','psalm':'psa','psalms':'psa','proverbs':'pro',
 'ecclesiastes':'ecc','song of solomon':'sng','isaiah':'isa','jeremiah':'jer','lamentations':'lam',
 'ezekiel':'eze','daniel':'dan','hosea':'hos','joel':'joe','amos':'amo','obadiah':'oba',
 'jonah':'jon','micah':'mic','nahum':'nah','habakkuk':'hab','zephaniah':'zep','haggai':'hag',
 'zechariah':'zec','malachi':'mal','matthew':'mat','mark':'mar','luke':'luk','john':'jhn',
 'acts':'act','romans':'rom','1 corinthians':'1co','2 corinthians':'2co','galatians':'gal',
 'ephesians':'eph','philippians':'phi','colossians':'col','1 thessalonians':'1th',
 '2 thessalonians':'2th','1 timothy':'1ti','2 timothy':'2ti','titus':'tit','philemon':'phm',
 'hebrews':'heb','james':'jam','1 peter':'1pe','2 peter':'2pe','1 john':'1jo','2 john':'2jn',
 '3 john':'3jn','jude':'jde','revelation':'rev',
}
LDS = {  # display-lower -> (volume, slug)
 '1 nephi':('bofm','1-ne'),'2 nephi':('bofm','2-ne'),'jacob':('bofm','jacob'),
 'enos':('bofm','enos'),'jarom':('bofm','jarom'),'omni':('bofm','omni'),
 'words of mormon':('bofm','w-of-m'),'mosiah':('bofm','mosiah'),'alma':('bofm','alma'),
 'helaman':('bofm','hel'),'3 nephi':('bofm','3-ne'),'4 nephi':('bofm','4-ne'),
 'mormon':('bofm','morm'),'ether':('bofm','ether'),'moroni':('bofm','moro'),
 'doctrine and covenants':('dc-testament','dc'),'d&c':('dc-testament','dc'),
 'moses':('pgp','moses'),'abraham':('pgp','abr'),
}
# Books that collide with common English words / non-scripture usage -> require a verse to link.
AMBIG = {'job','mark','acts','moses','abraham','jacob','ether','mormon','amos','omni','titus','jude','joel'}

def alt(keys):
    return "|".join(sorted((re.escape(k) for k in keys), key=len, reverse=True))
BIB_ALT = alt(BOOK_BLB.keys())
LDS_ALT = alt(LDS.keys())
# ref = book + space + chapter + optional :verse(-range).  dash may be -, en-dash, or &ndash;/&mdash;
REF = r"(?P<bk>{bks})\s+(?P<ch>\d+)(?::(?P<v>\d+)(?:(?:-|–|&ndash;|&mdash;)\d+)?)?"
TOKEN = re.compile(r'(<[^>]+>)')

def build_re(which):
    if which=='biblical': bks=BIB_ALT
    elif which=='lds':    bks=LDS_ALT
    else:                 bks=BIB_ALT+"|"+LDS_ALT
    return re.compile(REF.format(bks=bks), re.IGNORECASE)

def anchor(bk_disp, ch, v, text):
    low=bk_disp.lower()
    dataref = f"{bk_disp} {ch}" + (f":{v}" if v else "")
    if low in BOOK_BLB:
        vv = v or "1"
        url=f"https://www.blueletterbible.org/kjv/{BOOK_BLB[low]}/{ch}/{vv}/"
    else:
        vol,slug=LDS[low]
        url=f"https://www.churchofjesuschrist.org/study/scriptures/{vol}/{slug}/{ch}?lang=eng" + (f"&id={v}" if v else "")
    return f'<a href="{url}" target="_blank" data-ref="{dataref}">{text}</a>'

# canonical display casing
DISP={}
for k in list(BOOK_BLB)+list(LDS):
    DISP[k]= 'D&C' if k=='d&c' else k.title().replace(' Of ',' of ').replace(' And ',' and ')

def linkify_text(txt, rx, counter):
    out=[]; last=0
    for m in rx.finditer(txt):
        low=m.group('bk').lower(); v=m.group('v')
        if low in AMBIG and not v:      # skip ambiguous book-word with no verse
            continue
        disp=DISP[low]
        out.append(txt[last:m.start()])
        out.append(anchor(disp, m.group('ch'), v, m.group(0)))
        last=m.end(); counter[0]+=1
    out.append(txt[last:])
    return "".join(out)

FM_RE = re.compile(r'^(---\n.*?\n---\n)', re.DOTALL)

def process(content, rx):
    # Never touch YAML frontmatter (description: fields hold bare refs but cannot carry HTML)
    fm=""
    m=FM_RE.match(content)
    if m:
        fm=m.group(1); content=content[m.end():]
    body,n=_process_body(content, rx)
    return fm+body, n

def _process_body(content, rx):
    parts=TOKEN.split(content)
    in_a=in_s=False; counter=[0]
    for i,tok in enumerate(parts):
        if tok.startswith('<'):
            t=tok.lower()
            if t.startswith('<a ') or t=='<a>': in_a=True
            elif t.startswith('</a'): in_a=False
            elif t.startswith('<script'): in_s=True
            elif t.startswith('</script'): in_s=False
            continue
        if in_a or in_s: continue
        parts[i]=linkify_text(tok, rx, counter)
    return "".join(parts), counter[0]

def _process_body_unused():
    pass

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--write',action='store_true')
    ap.add_argument('--guide',default='*'); ap.add_argument('--set',default='biblical',choices=['biblical','lds','all'])
    ap.add_argument('--samples',type=int,default=0)
    a=ap.parse_args()
    rx=build_re(a.set)
    files=sorted(glob.glob(f"content/culture/ancient/{a.guide}/*.md")) + \
          sorted(glob.glob(f"content/culture/{a.guide}/*.md"))
    files=[f for f in files if '/ancient/' in f or a.guide!='*']
    if a.guide=='*':
        files=sorted(set(glob.glob("content/culture/ancient/*/*.md")))
    grand=0
    for f in files:
        s=open(f,encoding="utf-8").read()
        new,n=process(s,rx)
        grand+=n
        if n:
            print(f"{n:4}  {f}")
            if a.samples:
                # show first few new anchors
                added=re.findall(r'<a href="[^"]*"[^>]*data-ref="[^"]*">[^<]*</a>', new)
                # crude: show anchors not in original
                orig=set(re.findall(r'<a href="[^"]*"[^>]*data-ref="[^"]*">[^<]*</a>', s))
                shown=[x for x in added if x not in orig][:a.samples]
                for x in shown: print("        +", x)
        if a.write and n:
            open(f,"w",encoding="utf-8").write(new)
    print(f"\n{'WROTE' if a.write else 'DRY-RUN'} total {a.set} links: {grand}")

if __name__=="__main__": main()
