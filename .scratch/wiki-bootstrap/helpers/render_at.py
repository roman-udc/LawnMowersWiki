# usage: python render.py <draft.md> <page e.g. causes/x> <out.md>   (run from repo root)
# Draft tokens: @@slug@@ -> [Sn](../../raw/...) ; @@re:REGEX@@ -> all matching slugs joined ", "
# Sources numbered in notes order; ## Sources and source_count are filled in. Warns on uncited Sources.
import sys,re,subprocess,os
sys.stdout.reconfigure(encoding='utf-8')
draft,page,out=sys.argv[1:4]
r=subprocess.run([sys.executable,'.scratch/wiki-bootstrap/collect_notes.py','--sources',page],capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'}).stdout
rows=[l.split(' | ') for l in r.splitlines() if l.strip()]
num={};info={}
for i,(p,t,tier) in enumerate(rows,1):
    slug=p.rsplit('/',1)[1][:-3]; num[slug]=i; info[slug]=(p,t,tier)
used=set()
def link(s):
    if s not in num: sys.exit('unknown slug '+s)
    used.add(s); return f'[S{num[s]}](../../{info[s][0]})'
def sub(m):
    k=m.group(1)
    if k.startswith('re:'):
        ss=sorted([s for s in num if re.search(k[3:],s)],key=num.get)
        if not ss: sys.exit('no match '+k)
        return ', '.join(link(s) for s in ss)
    return link(k)
t=open(draft,encoding='utf-8').read()
t=re.sub(r'@@(.+?)@@',sub,t)
cited=sorted(used,key=num.get)
src='\n'.join(f'- {link(s)} — {info[s][1]} ({info[s][2]})' for s in cited)
# renumber densely in order of S-number so source list has only cited ones
t=t.rstrip('\n')+'\n\n## Sources\n\n'+src+'\n'
t=re.sub(r'^source_count: .*$',f'source_count: {len(cited)}',t,count=1,flags=re.M)
open(out,'w',encoding='utf-8',newline='\n').write(t)
unc=[s for s in num if s not in used]
print('cited',len(cited),'of',len(num),'uncited:',unc)
