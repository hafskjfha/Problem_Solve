import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
E=[[] for _ in range(N+1)]
P=[None]*(N+1)
for _ in range(N-1):
	a,b=map(int,input().split())
	E[a].append(b)
	E[b].append(a)
def bfs():
	q=deque([1])
	while q:
		O=q.popleft()
		for G in E[O]:
			if P[G]==None:
				q.append(G)
				P[G]=O
bfs()
for i in range(2,N+1):print(P[i])
