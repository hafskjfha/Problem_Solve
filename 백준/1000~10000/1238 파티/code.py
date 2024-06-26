import sys,heapq
input=sys.stdin.readline
N,M,X=map(int,input().split())
eg,reg=[[]for _ in range(N+1)],[[]for _ in range(N+1)]
for i in range(M):
	A,B,T=map(int,input().split())
	eg[A].append([T,B])
	reg[B].append([T,A])
def dijkstra(K,eg):
	d=[float('inf')]*(N+1)
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
	return d
d1=dijkstra(X,eg)
d2=dijkstra(X,reg)
d3=[d1[i]+d2[i]for i in range(1,N+1)]
print(max(d3))
