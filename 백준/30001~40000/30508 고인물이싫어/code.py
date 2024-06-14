import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
h,w=map(int,input().split())
e=[list(map(int,input().split())) for _ in range(N)]
def bfs(S,x,y):
	q=deque([S])
	e[y][x]=0
	while q:
		x,y,info=q.popleft()
		if info==0:continue
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<M and 0<=dy<N and e[dy][dx]!=0:
				if e[dy][dx]>=info:
					q.append((dx,dy,e[dy][dx]))
					e[dy][dx]=0
for _ in range(int(input())):
	a,b=map(int,input().split())
	if e[a-1][b-1]!=0:
		bfs((b-1,a-1,e[a-1][b-1]),b-1,a-1)
su=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,  N+ 1):
    for j in range(1, M + 1):
        su[i][j] = e[i - 1][j - 1]  + su[i-1][j] + su[i][j-1] - su[i -1][j - 1]
C=0
for i in range(1, N - h + 2):
	for j in range(1,M - w + 2):
		try:
			if su[i + h - 1][j + w - 1] - su[i + h - 1][j - 1] - su[i - 1][j + w - 1] + su[i - 1][j - 1]==0:
				C+=1
		except IndexError:
			continue
print(C)
