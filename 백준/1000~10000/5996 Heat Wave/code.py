import sys,heapq
input=sys.stdin.readline
T,C,Ts,Te=map(int,input().split())
eg,d=[[]for _ in range(T+1)],[float('inf')]*(T+1)
for i in range(C):
	u,v,w=map(int,input().split())
	eg[u].append([w,v])
	eg[v].append([w,u])
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
dijkstra(Ts)
print(d[Te])
