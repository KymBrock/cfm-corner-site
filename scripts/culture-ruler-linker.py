#!/usr/bin/env python3
"""
Link the FIRST unlinked prose mention of each ancient ruler (per file) to a
VERIFIED "learn more" source (World History Encyclopedia primary, Britannica
fallback). Every URL below was confirmed live via search — none guessed.

Disambiguation-safe: only exact, unambiguous name-strings are linked. Bare
ambiguous names (bare "Darius", bare "Shalmaneser", "Nebuchadnezzar I", etc.)
are deliberately NOT auto-linked. Tokenizes HTML so it never touches existing
anchors, <script>, headings, or <figcaption>.

Usage: python3 scripts/culture-ruler-linker.py --guide babylon [--write]
"""
import re, glob, argparse, os

WHE="https://www.worldhistory.org/"; BR="https://www.britannica.com/biography/"
# (regex for the name as it appears, URL). Order: most-specific first.
RULERS=[
 (r'Alexander the Great', WHE+"Alexander_the_Great/"),
 (r'Tiglath-[Pp]ileser III', WHE+"Tiglath_Pileser_III/"),
 (r'Shalmaneser III', BR+"Shalmaneser-III"),
 (r'Ashurnasirpal II', WHE+"Ashurnasirpal_II/"),
 (r'Tukulti-Ninurta I(?![IV])', WHE+"Tukulti-Ninurta_I/"),
 (r'Sargon II', WHE+"Sargon_II/"),
 (r'Darius the Great', WHE+"Darius_I/"),
 (r'Darius I(?![IV])', WHE+"Darius_I/"),
 (r'Artaxerxes I(?![IV])', WHE+"Artaxerxes_I/"),
 (r'Necho(?: II)?', BR+"Necho-II"),
 (r'Merodach-baladan', BR+"Merodach-Baladan-II"),
 (r'Shamash-shum-ukin', BR+"Shamash-shum-ukin"),
 (r'Nabopolassar', BR+"Nabopolassar"),
 (r'Nebuchadnezzar(?: II)?(?! I(?![IV]))', WHE+"Nebuchadnezzar_II/"),
 (r'Amel-Marduk', BR+"Awil-Marduk"),
 (r'Neriglissar', BR+"Nergal-shar-usur"),
 (r'Nabonidus', BR+"Nabonidus"),
 (r'Belshazzar', BR+"Belshazzar"),
 (r'Sennacherib', WHE+"sennacherib/"),
 (r'Esarhaddon', WHE+"Esarhaddon/"),
 (r'Ashurbanipal', WHE+"Ashurbanipal/"),
 (r'Hammurabi', WHE+"hammurabi/"),
 (r'Cyrus(?! Cylinder)\b', WHE+"Cyrus_the_Great/"),
 (r'Cambyses(?: II)?', WHE+"Cambyses_II/"),
 (r'Xerxes(?![ ]I{2,})\b', WHE+"Xerxes_I/"),
 (r'Croesus', WHE+"croesus/"),
 (r'Astyages', BR+"Astyages"),
]
TOKEN=re.compile(r'(<(?:[^>"\']|"[^"]*"|\'[^\']*\')*>)')
SKIP_OPEN=re.compile(r'<(a|script|style|h[1-3]|figcaption)\b', re.I)
SKIP_CLOSE=re.compile(r'</(a|script|style|h[1-3]|figcaption)>', re.I)

def link_first(content, pattern, url, dry):
    parts=TOKEN.split(content); depth=0; done=False; ctx=None
    for i,tok in enumerate(parts):
        if tok.startswith('<'):
            if SKIP_OPEN.match(tok) and not tok.rstrip().endswith('/>'): depth+=1
            elif SKIP_CLOSE.match(tok): depth=max(0,depth-1)
            continue
        if depth>0 or done: continue
        m=re.search(r'(?<![\w>])'+pattern, tok)
        if m:
            a=f'<a href="{url}" target="_blank">{m.group(0)}</a>'
            ctx=tok[max(0,m.start()-30):m.start()]+"[["+m.group(0)+"]]"+tok[m.end():m.end()+30]
            if not dry: parts[i]=tok[:m.start()]+a+tok[m.end():]
            done=True
    return ("".join(parts), ctx) if done else (content, None)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--guide',required=True); ap.add_argument('--write',action='store_true')
    a=ap.parse_args(); total=0
    for f in sorted(glob.glob(f'content/culture/ancient/{a.guide}/*.md')):
        s=open(f,encoding='utf-8').read()
        fm=re.match(r'^---\n.*?\n---\n', s, re.DOTALL); head=fm.group(0) if fm else ''; body=s[len(head):]
        added=[]
        for pat,url in RULERS:
            body,ctx=link_first(body, pat, url, dry=not a.write)
            if ctx: added.append((ctx,url)); total+=1
        if added:
            print(f"\n{f.split('/')[-1]}")
            for ctx,url in added: print(f"   {ctx.strip()[:64]:66} -> {url.split('/')[-2] or url}")
        if a.write and added:
            open(f,'w',encoding='utf-8').write(head+body)
    print(f"\n{'WROTE' if a.write else 'DRY-RUN'}: {total} ruler links in {a.guide}")

if __name__=='__main__': main()
