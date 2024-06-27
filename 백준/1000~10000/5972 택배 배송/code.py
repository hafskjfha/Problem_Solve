import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
eg,d=[[]for _ in range(N+1)],[float('inf')]*(N+1)
for i in range(M):
	a,b,c=map(int,input().split())
	eg[a].append([c,b])
	eg[b].append([c,a])
def dijkstra():
	d[1]=0
	heap=[[0,1]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
	print(d[N])
dijkstra()
