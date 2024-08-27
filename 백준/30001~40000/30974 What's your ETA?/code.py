import heapq
input=open(0).readline
INF=float('inf')
def eratos(N):
    isp=[1]*(N+1)
    isp[0]=isp[1]=0
    for i in range(2,3163):
        if isp[i]:
            for j in range(i*2,N+1,i):
                isp[j]=0
    return isp
    
def dijkstra(eg,N,P,D):
    push=heapq.heappush
    pop=heapq.heappop
    d=[INF]*(N+1)
    d[1]=0
    pq=[[0,1]]
    while pq:
        w,v=pop(pq)
        if d[v]!=w:continue
        for nw,nv in eg[v]:
            if d[nv]>w+nw and P[D[v-1]+D[nv-1]]:
                d[nv]=w+nw
                push(pq,[d[nv],nv])
    return d[N]

def main():
    P=eratos(10000000)
    N,M=map(int,input().split())
    D=[*map(int,input().split())]
    gr=[[]for _ in range(N+1)]
    for _ in range(M):
        u,v,w=map(int,input().split())
        gr[u].append([w,v])
        gr[v].append([w,u])
    ans=dijkstra(gr,N,P,D)
    print(ans if ans!=INF else 'Now where are you?')
        
main()
