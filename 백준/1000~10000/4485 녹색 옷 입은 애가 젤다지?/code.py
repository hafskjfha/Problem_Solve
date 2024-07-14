import sys,heapq;
input=sys.stdin.readline;
def dijkstra(N,gr):
    d=[[float('inf')]*N for _ in range(N)];
    d[0][0]=gr[0][0];
    heap=[[gr[0][0],0,0]];
    while heap:
        w,x,y=heapq.heappop(heap);
        if d[y][x]<w:continue;
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<N:
                if d[dy][dx]>w+gr[dy][dx]:
                    d[dy][dx]=w+gr[dy][dx];
                    heapq.heappush(heap,[d[dy][dx],dx,dy]);
    return d[N-1][N-1]

T=1
while 1:
    N=int(input());
    if N==0:break;
    ma=[];
    for _ in range(N):
        ma.append(list(map(int,input().split())));
    print(f'Problem {T}: {dijkstra(N,ma)}');
    T+=1;
