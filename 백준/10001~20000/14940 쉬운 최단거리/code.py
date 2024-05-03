import sys
from collections import deque
input = sys.stdin.readline
#sys.stdin=open('input.txt','r')
N, M = map(int, input().split())
an = [[-1]*M for _ in range(N)]
ma = [list(map(int, input().split())) for _ in range(N)]

def bfs(c,d,di):
    q=deque([(c,d,di)])
    while q:
        x,y,dis = q.popleft()
        if ma[y][x] == 4:
            continue
        else:
            ma[y][x] = 4
            an[y][x] = dis
            for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= dx < M and 0 <= dy < N and ma[dy][dx] != 4 and ma[dy][dx] != 0:
                    q.append((dx,dy,dis+1))
    return
for i in range(N):
    for j in range(M):
        if ma[i][j] == 2:
            sx,sy=j,i
        elif ma[i][j] == 0:
            an[i][j] = 0
bfs(sx,sy,0)

for a in an:
    for b in a:
        print(b,end=' ')
    print()
