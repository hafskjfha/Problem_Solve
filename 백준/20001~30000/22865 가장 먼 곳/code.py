import heapq
from collections import deque
INF=float('inf')
input=open(0).readline
N=int(input())
F=[*map(int,input().split())]
M=int(input())
eg=[[]for _ in range(N+1)]
for _ in range(M):
	D,E,L=map(int,input().split())
	eg[D].append([L,E])
	eg[E].append([L,D])
def dijkstra(K):
	d=[INF]*(N+1)
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
	q=deque(d)
	q.popleft()
	return q
s={}
a={}
A=[]
for p in F:
	if p in s:
	    A.append(s[p])
	    continue
	k=dijkstra(p)
	s[p]=k
	A.append(k)
j,b=0,0
B=[0]*N
for i in range(N):
    B[i]=min(A[0][i],A[1][i],A[2][i])
for i in range(N):
    if B[i]>j:
        j=B[i]
        b=i+1
print(b)
