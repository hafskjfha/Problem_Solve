import sys,heapq
input=sys.stdin.readline
N=int(input())
M=int(input())
eg,d=[[]for _ in range(N+1)],[float('inf')]*(N+1)
for i in range(M):
	u,v,w=map(int,input().split())
	eg[u].append([w,v])
X,K=map(int,input().split())
def dijkstra(K):
	d[K]=0
	R=[[]for _ in range(N+1)]
	heap=[[0,K,[K]]]
	while heap:
		w,v,r=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				R[nv]=r+[nv]
				heapq.heappush(heap,[d[nv],nv,r+[nv]])
	return R
R=dijkstra(X)
print(d[K])
print(len(R[K]))
print(*R[K])
