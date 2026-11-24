import re,random,sys,subprocess
page=sys.argv[1]; random.seed(int(sys.argv[2])); n=int(sys.argv[3])
t=open(f'wiki/{page}.md',encoding='utf-8').read()
body=t.split('\n## Sources\n')[0]
notes=subprocess.run([sys.executable,'.scratch/wiki-bootstrap/collect_notes.py',page],capture_output=True,text=True,encoding='utf-8').stdout
nb={b.split(' | ')[0]:b for b in re.split(r'^=== ',notes,flags=re.M)[1:]}
# sections
secs=re.split(r'^(## .*)$',body,flags=re.M)
items=[]
for i in range(1,len(secs),2):
    h=secs[i]; content=secs[i+1]
    for m in re.finditer(r'\[(S\d+)\]\(\.\./\.\./(raw/[^)]+)\)',content):
        # nearest paragraph/bullet containing
        start=content.rfind('\n',0,content.rfind('\n- ',0,m.start())+1) if False else 0
        items.append((h,m.group(1),m.group(2),m.start(),content))
for h,s,path,pos,content in random.sample(items,n):
    # claim: the bullet/para containing pos; if it's a Sources: line, whole section
    lines=content.split('\n'); acc=0
    for l in lines:
        if acc<=pos<=acc+len(l): claim=l;break
        acc+=len(l)+1
    if claim.startswith('Sources:'): claim='[SECTION] '+re.sub(r'\[S\d+\]\([^)]*\)','',content)[:900]
    else: claim=re.sub(r'\(\.\./\.\./raw/[^)]*\)','',claim)[:900]
    print('#####',h,s,path); print('CLAIM:',claim); print('NOTE:',nb.get(path,'*** NO NOTE FOR THIS PAGE ***')[:1500]); print()
