# usage: python render.py <draft.md> <page e.g. causes/x> [extra raw paths...]
# Draft uses @slug (basename of raw Source, no .md) for citations, e.g. "Sources: @a, @b".
# Sources numbered in collect_notes order (plus extras), kept if page exists. Writes wiki/<page>.md.
import sys,re,subprocess,os
sys.stdout.reconfigure(encoding='utf-8')
draft,page=sys.argv[1],sys.argv[2]; extra=sys.argv[3:]
out=subprocess.run([sys.executable,'.scratch/wiki-bootstrap/collect_notes.py','--sources',page],capture_output=True,text=True,encoding='utf-8').stdout
rows=[l.split(' | ') for l in out.splitlines() if l.strip()]
for e in extra:
    t=open(e,encoding='utf-8').read(); ti=re.search(r'^title: *"?(.*?)"?\s*$',t,re.M).group(1)
    rows.append([e,ti,'manufacturer' if 'searspartsdirect' in e else 'expert-blog'])
by={os.path.basename(r[0])[:-3]:r for r in rows}
t=open(draft,encoding='utf-8').read()
used=[]
def rep(m):
    s=m.group(1)
    if s not in by: sys.exit('unknown slug '+s)
    if s not in used: used.append(s)
    return s
re.sub(r'@([a-z0-9.\-]+[a-z0-9])',rep,t)
order=[os.path.basename(r[0])[:-3] for r in rows if os.path.basename(r[0])[:-3] in used]
num={s:i+1 for i,s in enumerate(order)}
t=re.sub(r'@([a-z0-9.\-]+[a-z0-9])',lambda m:f'[S{num[m.group(1)]}](../../{by[m.group(1)][0]})',t)
fix=lambda x:x.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
src='\n'.join(f'- [S{num[s]}](../../{by[s][0]}) — {fix(by[s][1])} ({by[s][2]})' for s in order)
t=t.replace('SOURCES_LIST',src).replace('SOURCE_COUNT',str(len(order)))
open(f'wiki/{page}.md','w',encoding='utf-8',newline='\n').write(t)
unused=[os.path.basename(r[0])[:-3] for r in rows if os.path.basename(r[0])[:-3] not in used]
print('sources',len(order),'unused',unused)
