# usage: python linkprob.py <notes.txt> <problem-slug> "<Problem title>" <match-regex> [--skip=slug,slug] [--map=a:b,c:d] [--only=path,path to drop] cause=default-bullet-text ...
# For each cause=text: adds the Problem to the Cause's `problems`; in "## Symptoms it produces" turns the first plain
# bullet matching <match-regex> (e.g. "Engine loses power") into a link, or adds "- [Title](...): text" if none;
# appends "Sources for <Title>: ..." (all Sources whose causes-named lists the cause) and adds new Sources to ## Sources.
# --drop=path,... ignores those Sources' notes blocks. --map renames labels (worn-drive-belt:worn-or-stretched-belt).
import re,sys,datetime
sys.stdout.reconfigure(encoding='utf-8')
notes,prob,title,rx=sys.argv[1:5]
opts={a.split('=',1)[0]:a.split('=',1)[1] for a in sys.argv[5:] if a.startswith('--')}
spec=[a.split('=',1) for a in sys.argv[5:] if not a.startswith('--')]
amap=dict(x.split(':') for x in opts.get('--map','').split(',') if x)
drop=set(x for x in opts.get('--drop','').split(',') if x)
t=open(notes,encoding='utf-8').read()
info={};named={}
for b in re.split(r'^=== ',t,flags=re.M)[1:]:
    path,ti,tier=b.split('\n')[0].split(' | ')[:3]
    if path in drop: continue
    info[path]=(ti.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"'),tier)
    for l in re.findall(r'^- causes-named: (.*)$',b,re.M):
        for x in l.split(','):
            x=amap.get(x.strip().split(' (')[0],x.strip().split(' (')[0])
            if x: named.setdefault(x,set()).add(path)
link=f'[{title}](../problems/{prob}.md)'
for cause,text in spec:
    p=f'wiki/causes/{cause}.md'; s=open(p,encoding='utf-8').read()
    head,src=s.split('\n## Sources\n')
    have={m.group(2):int(m.group(1)) for m in re.finditer(r'^- \[S(\d+)\]\(\.\./\.\./(raw/[^)]+)\)',src,re.M)}
    nxt=max(have.values())+1; add=[]
    paths=sorted(named.get(cause,[]))
    for q in paths:
        if q not in have:
            have[q]=nxt; add.append(f'- [S{nxt}](../../{q}) — {info[q][0]} ({info[q][1]})'); nxt+=1
    cites=', '.join(f'[S{have[q]}](../../{q})' for q in sorted(paths,key=lambda q:have[q]))
    fm_end=head.index('\n---\n',4); fm=head[:fm_end]; body=head[fm_end:]
    rel=f'../problems/{prob}.md'
    if rel not in fm:
        if re.search(r'^problems: \[\]',fm,re.M): fm=re.sub(r'^problems: \[\]',f'problems:\n  - {rel}',fm,flags=re.M)
        else: fm=re.sub(r'(^problems:\n(?:  - .*\n)*)',lambda m:m.group(1)+f'  - {rel}\n',fm+'\n',count=1,flags=re.M).rstrip('\n')
    fm=re.sub(r'^updated: .*$','updated: '+opts.get('--date','2026-11-24'),fm,flags=re.M)
    m=re.search(r'(## Symptoms it produces\n)(.*?)(?=\n## )',body,re.S)
    sec=m.group(2); how='added'
    bm=re.search(r'^- ('+rx+r')',sec,re.M|re.I)
    if bm and link not in sec:
        sec=sec[:bm.start(1)]+link+sec[bm.end(1):]; how='linked'
    elif link not in sec:
        sec=sec.rstrip('\n')+f'\n\n- {link}: {text}\n'
    else: how='present'
    sec=sec.rstrip('\n')+f'\n\nSources for {title}: {cites}\n'
    body=body[:m.start(2)]+sec+body[m.end(2):]
    src=src.rstrip('\n')+'\n'+('\n'.join(add)+'\n' if add else '')
    n=len(re.findall(r'^- \[S\d+\]',src,re.M))
    out=fm+body+'\n## Sources\n'+src
    out=re.sub(r'^source_count: \d+',f'source_count: {n}',out,count=1,flags=re.M)
    open(p,'w',encoding='utf-8',newline='\n').write(out)
    print(f'{cause}: {how}, +{len(add)} Sources, {len(paths)} cited, count {n}')
