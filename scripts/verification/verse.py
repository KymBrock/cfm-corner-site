import json, sys, re
d=json.load(open('/Users/kymberbrockbank/Developer/POM-Beta-Reader-main/data/scriptures_complete.json'))
B=d['books']
alias={}
for key,book in B.items():
    for n in {key, book.get('name','').lower(), book.get('abbr','').lower(), book.get('blb_abbr','').lower()}:
        if n: alias[n.replace(' ','').replace('.','')]=key
def find_book(name):
    n=name.lower().strip().replace(' ','').replace('.','').replace('&','and')
    n=n.replace('d&c','doctrine_and_covenants').replace('dandc','doctrine_and_covenants').replace('dc','doctrine_and_covenants')
    if n in alias: return alias[n]
    for k in B:
        if k.replace('_','')==n: return k
    raise KeyError(name)
def chapters_obj(book):
    b=B[book]
    return b.get('chapters') or b.get('sections')
def get(ref):
    m=re.match(r'^(.*?)\s+(\d+):(\d+)(?:-(\d+))?$', ref.strip())
    if not m:
        m2=re.match(r'^(.*?)\s+(\d+)$', ref.strip())
        book=find_book(m2.group(1)); chap=m2.group(2); v1=None; v2=None
    else:
        book=find_book(m.group(1)); chap=m.group(2); v1=int(m.group(3)); v2=int(m.group(4)) if m.group(4) else v1
    ch=chapters_obj(book)[str(chap)]; vs=ch['verses']
    keys=sorted(vs.keys(),key=int) if v1 is None else [str(x) for x in range(v1,v2+1)]
    out=[]
    for k in keys:
        t=vs[k]['text']; out.append((k, t.get('kjv') or t.get('lds') or ''))
    return book,chap,out
for ref in sys.argv[1:]:
    try:
        book,chap,verses=get(ref)
        print(f'=== {ref} ({book} {chap}) ===')
        for num,txt in verses: print(f'  v{num}: {txt}')
    except Exception as e:
        print(f'!!! {ref}: ERROR {e}')
