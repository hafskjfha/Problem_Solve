import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
vi,E,c=[0]*(N+1),[[]for _ in range(N+1)],0
def bfs(s):
	q=deque([s])
	while q:
		x=q.popleft()
		if vi[x]:continue
		vi[x]=1
		for f in E[x]:
			if not vi[f]:
				q.append(f)
for _ in range(M):
	u,v=map(int,input().split())
	E[u].append(v)
	E[v].append(u)
for i in range(1,N+1):
	if not vi[i]:
		bfs(i)
		c+=1
print(c)
