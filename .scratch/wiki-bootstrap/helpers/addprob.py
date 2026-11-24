import re,sys
notes_path,prob,label=sys.argv[1],sys.argv[2],sys.argv[3]
spec=dict(a.split('=',1) for a in sys.argv[4:])  # cause=bullet text
notes=open(notes_path,encoding='utf-8').read()
blocks=re.split(r'^=== ',notes,flags=re.M)[1:]
info={}
named={}
for b in blocks:
    head=b.split('\n')[0].split(' | ')
    path,title,tier=head[0],head[1],head[2]
    info[path]=(title,tier)
    names=set()
    for l in re.findall(r'^- causes-named: (.*)$',b,re.M):
        names|={ {'bad-battery':'weak-or-dead-battery'}.get(x.strip(),x.strip()).split(' (')[0] for x in l.split(',')}
    for n in names: named.setdefault(n,[]).append(path)
for cause,bullet in spec.items():
    p=f'wiki/causes/{cause}.md'; t=open(p,encoding='utf-8').read()
    src=re.search(r'\n## Sources\n(.*)$',t,re.S).group(1)
    have={m.group(2):m.group(1) for m in re.finditer(r'^- \[(S\d+)\]\(\.\./\.\./(raw/[^)]+)\)',src,re.M)}
    nxt=max(int(s[1:]) for s in have.values())+1
    add=[]
    cites=[]
    for path in sorted(named.get(cause,[])):
        if path not in have:
            have[path]=f'S{nxt}'; title,tier=info[path]
            add.append(f'- [S{nxt}](../../{path}) — {title} ({tier})'); nxt+=1
    for path in sorted(named.get(cause,[]),key=lambda x:int(have[x][1:])):
        cites.append(f'[{have[path]}](../../{path})')
    # frontmatter problems
    fm_end=t.index('\n---\n',4)
    fm=t[:fm_end]
    rel=f'../problems/{prob}.md'
    if rel not in fm:
        fm=re.sub(r'(problems:\n(?:  - .*\n)*)',lambda m:m.group(1)+f'  - {rel}\n',fm+'\n',count=1).rstrip('\n')
    t=fm+t[fm_end:]
    # symptoms
    m=re.search(r'(## Symptoms it produces\n)(.*?)(\nSources:[^\n]*)(\n)',t,re.S)
    body=m.group(2).rstrip('\n')+f'\n{bullet}\n'
    srcline=m.group(3)+f'; {label} '+', '.join(cites)
    t=t[:m.start()]+m.group(1)+body+srcline+m.group(4)+t[m.end():]
    t=t.rstrip('\n')+'\n'+('\n'.join(add)+'\n' if add else '')
    n=len(re.findall(r'^- \[S\d+\]',t.split('\n## Sources\n')[1],re.M))
    t=re.sub(r'^source_count: \d+',f'source_count: {n}',t,count=1,flags=re.M)
    open(p,'w',encoding='utf-8',newline='\n').write(t)
    print(cause,'added',len(add),'count',n,'cites',len(cites))
