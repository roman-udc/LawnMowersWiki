import subprocess,re,glob,collections,os
def srcs(t):
    if '\n## Sources\n' not in t: return set()
    return set(re.findall(r'\]\(\.\./\.\./(raw/[^)]+)\)',t.split('\n## Sources\n')[1]))
m=collections.defaultdict(list)
for f in sorted(glob.glob('wiki/*/*.md')):
    f=f.replace(os.sep,'/'); rel=f[5:]
    now=srcs(open(f,encoding='utf-8').read())
    r=subprocess.run(['git','show','HEAD:'+f],capture_output=True,text=True,encoding='utf-8')
    old=srcs(r.stdout) if r.returncode==0 else set()
    for s in now-old: m[s].append(rel)
for s in sorted(m): print(f'- {s} → ingested → '+', '.join(m[s]))
