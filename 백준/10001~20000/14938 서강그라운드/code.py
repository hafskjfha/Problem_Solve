import heapq
N,M,R=map(int,input().split())
eg=[[]for _ in range(N+1)]
T=list(map(int,input().split()))
for i in range(R):
	A,B,I=map(int,input().split())
	eg[A].append([I,B])
	eg[B].append([I,A])
def dijkstra(K):
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
ma=0
for K in range(1,N+1):
	D=dijkstra(K)
	w=0
	for j in range(1,N+1):
		if D[j]<=M:
			w+=T[j-1]
	ma=max(ma,w)
print(ma)
