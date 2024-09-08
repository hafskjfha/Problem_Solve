from heapq import heappush,heappop
input=open(0).readline
INF=float('inf')

def dijkstra(K:int,N:int,gr:list[list[tuple[int,int]]])->list[int|float]:
    d:list[int|float]=[INF]*(N+1)
    d[K]=0
    pq:list[tuple[int,int]]=[(0,K)]
    while pq:
        w,v=heappop(pq)
        if d[v]!=w:continue
        for nw,nv in gr[v]:
            if d[nv]>w+nw:
                d[nv]=w+nw
                heappush(pq,(d[nv],nv))
    return d
        
def main() -> int:
    N,M,K=map(int,input().split())
    gr:list[list[tuple[int,int]]]=[[]for _ in range(N+1)]
    for _ in range(M):
        u,v,c=map(int,input().split())
        gr[u].append((c,v))
        gr[v].append((c,u))
    el=[*map(int,input().split())]
    d1=dijkstra(1,N,gr)
    dn=dijkstra(N,N,gr)
    ans:float|int=INF
    for i,p in enumerate(el,start=1):
        if p==-1:continue
        ans=min(ans,p*(K-1)+dn[i]+d1[i])
    print(ans if ans!=INF else -1)
    return 1


main()
