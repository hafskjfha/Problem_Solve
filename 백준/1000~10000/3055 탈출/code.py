import sys
from collections import deque
input=sys.stdin.readline
H,W=map(int,input().split())
m=[list(input().strip()) for _ in range(H)]
v,b=[[0]*W for _ in range(H)],[]
def bfs(S):
    q=deque(S)
    while q:
        x,y,d,info=q.popleft()
        if v[y][x]:continue
        if m[y][x]=='D':return d
        if info=='*':m[y][x]='*'
        v[y][x]=1
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<W and 0<=dy<H:
                if info=="*":
                    if m[dy][dx]=='.':
                        q.append((dx,dy,d+1,'*'))
                        m[dy][dx]='N'
                elif info=='G':
                    if m[dy][dx] in (".","D"):
                        q.append((dx,dy,d+1,"G"))
    return 'KAKTUS'
for i in range(W):
    for j in range(H):
        k=m[j][i]
        if k=='S':
            s=(i,j,0,'G')
        elif k=='*':
            b.append((i,j,0,'*'))
b.append(s)
print(bfs(b))
