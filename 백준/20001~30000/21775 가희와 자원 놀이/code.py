import sys
from collections import deque
input=open(0).readline
N,T=map(int,input().split())
turn=[*map(int,input().split())]
C=deque([input().strip().split()for _ in range(T)])
notgo=set()
cdi={}
for i in range(T):
    k=turn[i]
    if (p:=cdi.get(k,False)):
        ci,m=p[0],p[1]
        if m not in notgo:
            del cdi[k]
            print(ci)
            notgo.add(m)
            continue
        else:
            print(ci)
            continue
    else:
        id,name,*p=C.popleft()
        if name=='next':
            print(id)
        elif name=='acquire':
            if p[0] in notgo:
                cdi[k]=[id,p[0]]
                print(id)
            else:
                notgo.add(p[0])
                print(id)
        elif name=='release':
            notgo.discard(p[0])
            print(id)
