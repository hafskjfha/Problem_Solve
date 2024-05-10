import sys
from collections import deque
input=sys.stdin.readline
N,M,A,B,K=map(int,input().split())
m=[[0]*M for _ in range(N)]
for _ in range(K):
    c,d=map(int,input().split())
    m[c-1][d-1]=1
S,s=map(int,input().split())
E,e=map(int,input().split())
def bfs(p):
    q=deque([p])
    while q:
        x,y,d=q.popleft()
        if (x,y)==(e-1,E-1):return d
        if m[y][x]==4:continue
        m[y][x]=4
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<M and 0<=dy<N and 0<=dx+B-1<M and 0<=dy+A-1<N and m[dy][dx] not in (1,4) and ch(dx,dy) :
                q.append((dx,dy,d+1))
    return -1
def ch(sx,sy):
    for i in range(1,B):
        for j in range(1,A):
            if 0<=sx+i<M and 0<=sy+j<N:
                if m[sy+j][sx+i]==1 or m[sy+j][sx]==1 or m[sy][sx+i]==1:
                    return 0
    return 1
print(bfs((s-1,S-1,0)))
