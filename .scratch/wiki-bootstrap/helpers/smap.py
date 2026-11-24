# usage: python smap.py <slug>  (run from repo root). Prints S-number map: existing page S-numbers kept, new Sources appended.
import sys,re,subprocess,os
sys.stdout.reconfigure(encoding='utf-8')
slug=sys.argv[1]; page=f"wiki/causes/{slug}.md"
existing={}
if os.path.exists(page):
    for m in re.finditer(r"^- \[S(\d+)\]\(\.\./\.\./(raw/[^)]+)\)",open(page,encoding='utf-8').read(),re.M):
        existing[m.group(2)]=int(m.group(1))
out=subprocess.run([sys.executable,".scratch/wiki-bootstrap/collect_notes.py","--sources",f"causes/{slug}"],capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'}).stdout
rows=[l.split(" | ") for l in out.splitlines() if l.strip()]
n=max(existing.values(),default=0)
for r in rows:
    if r[0] not in existing: n+=1; existing[r[0]]=n
info={r[0]:r for r in rows}
for p,s in sorted(existing.items(),key=lambda x:x[1]):
    r=info.get(p,[p,"?","?"]); flag="" if p in info else "  [NO NOTES]"
    t=r[1].replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')
    if len(sys.argv)>2: print(f"- [S{s}](../../{p}) — {t} ({r[2]}){flag}")
    else: print(f"S{s}\t{p}\t{t}\t{r[2]}{flag}")
