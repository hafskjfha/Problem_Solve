import sys,heapq
input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())
eg,d=[[]for _ in range(V+1)],[float('inf')]*(V+1)
for i in range(E):
	u,v,w=map(int,input().split())
	eg[u].append([w,v])
def dijkstra(K):
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
dijkstra(K)
for j in range(1,V+1):
	print('INF')if d[j]==float('inf') else print(d[j])
