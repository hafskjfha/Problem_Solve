import heapq
input=open(0).readline
push=heapq.heappush
pop=heapq.heappop
def dijkstra(N,M,gr):
    d=[[float('inf')]*N for _ in range(M)]
    d[0][0]=0
    pq=[(0,0,0)]
    while pq:
        w,x,y=pop(pq)
        if d[y][x]<w:continue
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<M:
                if d[dy][dx]>w+gr[dy][dx]:
                    d[dy][dx]=w+gr[dy][dx]
                    push(pq,(d[dy][dx],dx,dy))
    return d[M-1][N-1]
N,M=map(int,input().split())
print(dijkstra(N,M,[[*map(int,list(input().strip()))]for _ in range(M)]))
