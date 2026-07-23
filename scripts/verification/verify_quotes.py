import json, re, sys, glob, unicodedata
DB=json.load(open('/Users/kymberbrockbank/Developer/POM-Beta-Reader-main/data/scriptures_complete.json'))
B=DB['books']
alias={}
for key,book in B.items():
    for n in {key, book.get('name','').lower(), book.get('abbr','').lower(), book.get('blb_abbr','').lower()}:
        if n: alias[n.replace(' ','').replace('.','').replace('-','')]=key

def find_book(name):
    n=name.lower().strip().replace(' ','').replace('.','').replace('-','')
    n=n.replace('d&c','doctrineandcovenants').replace('dc','doctrineandcovenants')
    n=n.replace('doctrineandcovenants','doctrine_and_covenants')
    if n in alias: return alias[n]
    # partial contains
    for a,k in alias.items():
        if a and (a.startswith(n) or n.startswith(a)) and len(n)>=3: return k
    raise KeyError(name)

def verses_text(book, chap, v1, v2):
    bk=B[book]
    container = bk.get('chapters') or bk.get('sections')
    ch=container.get(str(chap))
    vs=ch['verses']
    out=[]
    keys=[str(x) for x in range(v1, (v2 or v1)+1)]
    for k in keys:
        if k in vs:
            t=vs[k]['text']; out.append(t.get('kjv') or t.get('lds') or '')
    return ' '.join(out)

def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-')
    s=s.lower()
    s=re.sub(r"[^a-z0-9' ]",' ',s)
    s=re.sub(r'\s+',' ',s).strip()
    return s

refpat=re.compile(r'^\s*([1-4]?\s*[A-Za-z&.]+(?:\s[A-Za-z]+)?)\s+(\d+):(\d+)(?:[-–](\d+))?')

def parse_ref(ref):
    m=refpat.match(ref)
    if not m: return None
    book=find_book(m.group(1))
    return book, int(m.group(2)), int(m.group(3)), (int(m.group(4)) if m.group(4) else None)

# extract "quote" (ref) pairs
pair=re.compile(r'"([^"]{6,}?)"\s*\(([^)]{2,40})\)')
total=0; flagged=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.md')):
    fn=f.split('/')[-1]
    t=open(f,encoding='utf-8').read()
    for m in pair.finditer(t):
        quote, ref = m.group(1), m.group(2)
        if not re.search(r'\d+:\d+', ref): continue
        total+=1
        segs=[norm(s) for s in re.split(r'\.\.\.|…', quote) if norm(s)]
        # strip markdown bold/emphasis leftovers
        segs=[s.replace('*','').strip() for s in segs]; segs=[s for s in segs if s]
        # candidate books: explicit book in ref, else try Ezra/Nehemiah + a few OT
        bm=refpat.match(ref)
        candidates=[]
        if bm and bm.group(1) and not bm.group(1).strip().isdigit():
            try: candidates=[find_book(bm.group(1))]
            except: candidates=[]
        if not candidates:
            m2=re.match(r'\s*(\d+):(\d+)(?:[-–](\d+))?', ref)
            if m2:
                ch=int(m2.group(1)); v1=int(m2.group(2)); v2=int(m2.group(3)) if m2.group(3) else None
                candidates=[('ezra',ch,v1,v2),('nehemiah',ch,v1,v2),('2_chronicles',ch,v1,v2),('haggai',ch,v1,v2),('zechariah',ch,v1,v2)]
        else:
            m2=re.search(r'(\d+):(\d+)(?:[-–](\d+))?', ref)
            ch=int(m2.group(1)); v1=int(m2.group(2)); v2=int(m2.group(3)) if m2.group(3) else None
            candidates=[(candidates[0],ch,v1,v2)]
        matched=False
        for cand in candidates:
            try:
                bk,ch,v1,v2=cand
                vt=norm(verses_text(bk,ch,v1,v2))
                if vt and all(s in vt for s in segs):
                    matched=True; break
            except Exception:
                pass
        if not matched:
            flagged.append((fn,ref,quote,'NO-MATCH in '+','.join(c[0] for c in candidates)))
print(f'checked {total} quoted-with-citation passages')
print(f'flagged {len(flagged)} for manual review:\n')
for fn,ref,quote,why in flagged:
    print(f'[{fn}] ({ref})')
    print(f'   quote: "{quote[:100]}"')
    print(f'   -> {why}\n')
