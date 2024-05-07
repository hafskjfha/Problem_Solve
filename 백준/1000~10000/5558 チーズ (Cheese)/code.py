import sys
from collections import deque
input=sys.stdin.readline
H,W,N=map(int,input().split())
m,a,r=[list(input().strip()) for _ in range(H)],0,0
def bfs(S,t):
	q,v=deque([S]),[[0]*W for _ in range(H)]
	while q:
		x,y,d=q.popleft()
		if v[y][x]==1:continue
		if m[y][x]==str(t):return (x,y,0),d
		v[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]!='X' and not v[dy][dx]:
				q.append((dx,dy,d+1))
for i in range(W):
	for j in range(H):
		if m[j][i]=='S':
			u=(i,j,0)
			break
	else:
		continue
	break
for k in range(1,N+1):
	u,r=bfs(u,k)
	a+=r
print(a)
