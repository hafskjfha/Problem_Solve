import heapq;
input=open(0).readline;
def dijkstra(N:int,gr:list[list[int]])->int:
    d:list[list[float|int]]=[[float('inf')]*N for _ in range(N)];
    d[0][0]=0;
    heap:list[tuple[int|float,int,int]]=[(0,0,0)];
    while heap:
        w,x,y=heapq.heappop(heap);
        if d[y][x]<w:continue;
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<N:
                p:int=0 if gr[dy][dx] else 1;
                if d[dy][dx]>w+p:
                    d[dy][dx]=w+p;
                    heapq.heappush(heap,(d[dy][dx],dx,dy));
    return d[N-1][N-1];

def main()->int:
    N=int(input());
    ma=[[*map(int,list(input().strip()))]for _ in range(N)];
    print(dijkstra(N,ma));
    return 1;

main()
