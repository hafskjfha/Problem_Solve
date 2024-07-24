import sys,heapq;
input=sys.stdin.readline;
INF=1e14
def dijkstra(W,H,gr,sx,sy,clas):
    d=[[INF]*W for _ in range(H)];
    d[sy][sx]=0;
    heap=[[0,sx,sy]];
    while heap:
        w,x,y=heapq.heappop(heap);
        if d[y][x]<w:continue;
        if not x or x==W-1 or not y or y==H-1:return w
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<W and 0<=dy<H:
                if d[dy][dx]>w+clas[gr[dy][dx]]:
                    d[dy][dx]=w+clas[gr[dy][dx]];
                    heapq.heappush(heap,[d[dy][dx],dx,dy]);
def main():
    for _ in range(int(input())):
        K,W,H=map(int,input().split())
        clas={'E':0}
        for _ in range(K):
            cn,t=input().strip().split()
            clas[cn]=int(t)
        m=[]
        f=0
        for i in range(H):
            temp=list(input().strip())
            if not f:
                for j in range(W):
                    if temp[j]=='E':
                        sx=j
                        sy=i
                        f=1
            m.append(temp)
        print(dijkstra(W,H,m,sx,sy,clas));
main()
