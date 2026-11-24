# usage: python expand.py <draft> <out> <notes.txt> slug1 slug2 ...  (slug order = S-numbers)
# Draft uses {slug} tokens; expands to [Sn](../../raw/...) and appends ## Sources from notes headers.
import sys,re
draft,out,notes=sys.argv[1:4]; order=sys.argv[4:]
info={}
for l in open(notes,encoding='utf-8'):
    if l.startswith('=== '):
        p,t,tier=l[4:].split(' | ')[:3]; info[p.rsplit('/',1)[1][:-3]]=(p,t,tier)
num={s:i+1 for i,s in enumerate(order)}
t=open(draft,encoding='utf-8').read()
used=set()
def rep(m):
    s=m.group(1); used.add(s); return f'[S{num[s]}](../../{info[s][0]})'
t=re.sub(r'\{([a-z0-9.\-]+)\}',rep,t)
unused=[s for s in order if s not in used]
if unused: print('UNUSED',unused)
src='\n'.join(f'- [S{num[s]}](../../{info[s][0]}) — {info[s][1]} ({info[s][2]})' for s in order)
t=t.replace('SOURCE_COUNT',str(len(order)))+'\n## Sources\n\n'+src+'\n'
open(out,'w',encoding='utf-8',newline='\n').write(t)
