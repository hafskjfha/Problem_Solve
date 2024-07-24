import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
gr=[[]for _ in range(N+1)]
di=[[-1]*(N+1)for _ in range(N+1)]
for _ in range(N-1):
	X,Y,D=map(int,input().split())
	gr[X].append([Y,D])
	gr[Y].append([X,D])
def bfs(st):
	q=deque([[st,0]])
	di[st][st]=0
	while q:
		node,d=q.popleft()
		for nn,nd in gr[node]:
			if di[st][nn]==-1:
				di[st][nn]=d+nd
				q.append([nn,d+nd])
for i in range(1,N+1):
	bfs(i)
for _ in range(M):
	A,B=map(int,input().split())
	print(di[A][B])
