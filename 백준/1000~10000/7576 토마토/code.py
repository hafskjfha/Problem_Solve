import sys
from collections import deque
input=sys.stdin.readline
M,N=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(N)]
def bfs(S):
	q,a=deque(S),0
	while q:
		x,y,di=q.popleft()
		if b[y][x]==2:
			continue
		b[y][x],a=2,max(a,di)
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<M and 0<=dy<N and b[dy][dx]==0:
				q.append((dx,dy,di+1))
	if a==0:
		return 0
	return a
p=[]
for i in range(M):
	for j in range(N):
		if b[j][i]==1:
			p.append((i,j,0))
if not p:
    print(-1)
    sys.exit()
e=bfs(p)
if e==0:
	print(0)
else:
	for i in range(M):
		for j in range(N):
			if b[j][i]==0:
				print(-1)
				sys.exit()
	print(e)
