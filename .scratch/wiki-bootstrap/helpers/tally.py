import re,sys,collections
t=open(sys.argv[1],encoding='utf-8').read()
blocks=re.split(r'^=== ',t,flags=re.M)[1:]
c=collections.Counter();m=collections.Counter();tiers=collections.Counter();types=collections.Counter();al=[]
for b in blocks:
    head=b.split('\n')[0];tier=head.split(' | ')[2];tiers[tier]+=1
    ty=re.search(r"types: \[(.*)\]",head); 
    for x in (ty.group(1) if ty else '').replace("'","").split(','): types[x.strip()]+=1
    names=set()
    for l in re.findall(r'^- causes-named: (.*)$',b,re.M):
        names|={{'bad-battery':'weak-or-dead-battery'}.get(x.strip(),x.strip()).split(' (')[0] for x in l.split(',') if x.strip()}
    for n in names:
        c[n]+=1
        if tier=='manufacturer': m[n]+=1
    al+=re.findall(r'^- alias: (.*)$',b,re.M)
print(len(blocks),tiers,types)
for n,k in sorted(c.items(),key=lambda x:(-x[1],-m[x[0]],x[0])): print(k,m[n],n)
print(len(al)); print('\n'.join(sorted(set(al))))
