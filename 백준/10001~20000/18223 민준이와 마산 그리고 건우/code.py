import sys,heapq
input=sys.stdin.readline
V,E,P=map(int,input().split())
eg=[[]for _ in range(V+1)]
for i in range(E):
	a,b,c=map(int,input().split())
	eg[a].append([c,b])
	eg[b].append([c,a])
def dijkstra(K):
	d=[float('inf')]*(V+1)
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
A=dijkstra(1)
G=dijkstra(P)
print('SAVE HIM')if A[V]==A[P]+G[V]else print('GOOD BYE')
