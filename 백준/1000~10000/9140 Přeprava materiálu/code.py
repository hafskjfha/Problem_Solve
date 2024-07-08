import sys,heapq
input=sys.stdin.readline
def dijkstra(K,N,eg):
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
while 1:
	N,M,S,C=map(int,input().split())
	if (N,M,S,C)==(0,0,0,0):break
	eg=[[]for _ in range(N+1)]
	for _ in range(M):
		A,B,V=map(int,input().split())
		eg[A].append([V,B])
	print(dijkstra(S,N,eg)[C])
