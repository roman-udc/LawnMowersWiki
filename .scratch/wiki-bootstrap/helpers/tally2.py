# usage: python tally2.py <notes.txt> [alias=slug ...]
# Like tally.py, but resolves "label (slug)" / "x / slug" items to the slug, maps extra aliases, drops non-slug labels.
# Prints: count, manufacturer count, slug, then Sources per slug with --paths.
import re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
args=[a for a in sys.argv[2:] if '=' in a]; amap=dict(a.split('=',1) for a in args)
amap.setdefault('bad-battery','weak-or-dead-battery')
t=open(sys.argv[1],encoding='utf-8').read()
blocks=re.split(r'^=== ',t,flags=re.M)[1:]
slug=re.compile(r'^[a-z0-9]+(-[a-z0-9]+)+$')
def res(x):
    x=x.strip()
    if not x: return None
    for cand in [x.split(' (')[0].strip()]+re.findall(r'\(([^)]*)\)',x)+[p.strip() for p in x.split('/')]:
        cand=amap.get(cand.strip(),cand.strip())
        if slug.match(cand) and cand!='unmapped': return cand
    return amap.get(x)
c=collections.Counter();m=collections.Counter();who=collections.defaultdict(list);drop=collections.Counter()
for b in blocks:
    head=b.split('\n')[0];path,title,tier=head.split(' | ')[:3]
    names=set()
    for l in re.findall(r'^- causes-named: (.*)$',b,re.M):
        for x in re.split(r',(?![^(]*\))',l):
            r=res(x)
            if r: names.add(r)
            elif x.strip(): drop[x.strip()]+=1
    for n in names:
        c[n]+=1; who[n].append(path)
        if tier=='manufacturer': m[n]+=1
print('blocks',len(blocks))
for n,k in sorted(c.items(),key=lambda x:(-x[1],-m[x[0]],x[0])): print(k,m[n],n)
print('dropped labels:',dict(drop))
if '--paths' in sys.argv:
    for n in who: print('##',n); print('\n'.join(who[n]))
