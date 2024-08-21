import heapq
INF=float('inf')
input=open(0).readline
def dijkstra(N,gr):
    d=[[INF]*N for _ in range(N)]
    d[0][0]=0
    heap=[[0,0,0]]
    while heap:
        w,x,y=heapq.heappop(heap)
        if d[y][x]<w:continue
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<N:
                nw=max(w,abs(gr[y][x]-gr[dy][dx]))
                if d[dy][dx]>nw :
                    d[dy][dx]=nw
                    heapq.heappush(heap,[nw,dx,dy])
    return d[N-1][N-1]
   
def main():
    N=int(input())
    gr=[[*map(int,input().split())]for _ in range(N)]
    print(dijkstra(N,gr))
main()
