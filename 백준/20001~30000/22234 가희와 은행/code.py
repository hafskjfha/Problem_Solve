from collections import deque
input=open(0).readline
N,T,W=map(int,input().split())
q=deque([[*map(int,input().split())]for _ in range(N)])
a=deque(sorted([[*map(int,input().split())]for _ in range(int(input()))],key=lambda x:x[2]))
r=0
while W-r:
    p,t=q.popleft()
    for _ in range(T):
        print(p)
        t-=1
        r+=1
        if a and a[0][2]==r:
            k,i,c=a.popleft()
            q.append([k,i])
        if W-r==0 or t==0:
            break
    if t:
        q.append([p,t])
