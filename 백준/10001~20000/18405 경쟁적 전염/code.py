import sys
from collections import deque
input=sys.stdin.readline
def bfs(R,ti):
    q=deque(R)
    while q:
        x,y,na,tim=q.popleft()
        if vi[y][x]:
            continue
        tt[y][x],vi[y][x] = na,True
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<N and tt[dy][dx] == 0:
                if tim+1 <= ti:
                    q.append((dx,dy,na,tim+1))


N,T=map(int,input().split())
tt = [list(map(int,input().split())) for _ in range(N)]
vi=[[False]*N for _ in range(N)]
S,X,Y = map(int,input().split())
s=[]
for i in range(N):
    for j in range(N):
        info = tt[j][i]
        if info != 0:
            s.append((i,j,info,0))
s.sort(key=lambda x:x[2])
bfs(s,S)
print(tt[X-1][Y-1])
