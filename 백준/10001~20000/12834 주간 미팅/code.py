import heapq
INF=float('inf')
input=open(0).readline
N,V,E=map(int,input().split())
A,B=map(int,input().split())
H=[*map(int,input().split())]
eg=[[]for _ in range(V)]
for i in range(E):
	a,b,I=map(int,input().split())
	eg[a-1].append([I,b-1])
	eg[b-1].append([I,a-1])
def dijkstra(K):
    d=[INF]*(V)
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
G=dijkstra(A-1)
K=dijkstra(B-1)
S=0
for i in H:
    t=0
    t+=G[i-1] if G[i-1]!=INF else -1
    t+=K[i-1] if K[i-1]!=INF else -1
    S+=t
print(S)
