from collections import deque
input=open(0).readline
def bfs(gr,p):
    q=deque([1])
    if 1 in p:return 1
    p.add(1)
    while q:
        a=q.popleft()
        if not gr[a]:
            return 0
        for n in gr[a]:
            if n not in p:
                p.add(n)
                q.append(n)
    return 1
N,M=map(int,input().split())
gr=[[]for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    gr[u].append(v)
input()
p=set(map(int,input().split()))
print('Yes'if bfs(gr,p)else'yes')
