import sys,heapq
input=sys.stdin.readline
N,E=map(int,input().split())
eg=[[]for _ in range(N+1)]
for i in range(E):
	a,b,c=map(int,input().split())
	eg[a].append([c,b])
	eg[b].append([c,a])
V1,V2=map(int,input().split())
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
D=dijkstra(1)
c1,c2=D[V1],D[V2]
D1=dijkstra(V1)
D2=dijkstra(V2)
c1+=D1[V2]+D2[N]
c2+=D2[V1]+D1[N]
print(A)if (A:=min(c1,c2))!=float('inf')else print(-1)
