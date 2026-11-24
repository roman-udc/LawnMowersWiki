# usage: python render_problem.py <draft.md> <notes-page e.g. problems/uneven-cut> <out.md> [D:slug=value ...]
# Replaces {{slug}} (Source basename without .md) with [Sn](../../raw/...) using the notes Source order,
# fills {{D:slug}} placeholders from args, and appends the ## Sources list. Fails on unknown slugs.
import re,sys,subprocess,os
sys.stdout.reconfigure(encoding='utf-8')
draft,page,out=sys.argv[1:4]; dv={k.removeprefix('D:'):v for k,v in (a.split('=',1) for a in sys.argv[4:])}
rows=[l.split(' | ') for l in subprocess.run([sys.executable,'.scratch/wiki-bootstrap/collect_notes.py','--sources',page],capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'}).stdout.splitlines() if l.strip()]
smap={}
for i,r in enumerate(rows,1): smap[os.path.basename(r[0])[:-3]]=(i,r[0],r[1],r[2])
t=open(draft,encoding='utf-8').read()
t=re.sub(r'\{\{D:([^}]+)\}\}',lambda m:dv[m.group(1)],t)
def rep(m):
    i,p,_,_=smap[m.group(1)]; return f'[S{i}](../../{p})'
t=re.sub(r'\{\{([^}]+)\}\}',rep,t)
q=lambda s:s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
t=t.rstrip('\n')+'\n\n'+'\n'.join(f'- [S{i}](../../{p}) — {q(ti)} ({tier})' for i,p,ti,tier in smap.values())+'\n'
open(out,'w',encoding='utf-8',newline='\n').write(t)
print('sources',len(smap))
