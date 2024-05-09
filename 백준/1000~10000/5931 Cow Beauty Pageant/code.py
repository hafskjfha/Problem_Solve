import sys
from collections import deque
input=sys.stdin.readline
H,W=map(int,input().split())
INF=float('inf')
m,v=[list(input().strip()) for _ in range(H)],[[INF]*W for _ in range(H)]
def Bfs(S):
	q=deque([S])
	while q:
		x,y=q.popleft()
		if m[y][x]==1:continue
		m[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]=='X':
				q.append((dx,dy))
def bfs(S):
	q,a=deque([S]),INF
	while q:
		x,y,d=q.popleft()
		if m[y][x]=='X':
			a=min(a,d)
			continue
		if v[y][x]==INF:
			v[y][x]=d
		else:
			if v[y][x]<=d:
				continue
			v[y][x]=d
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H:
				p=m[dy][dx]
				if p==1:
					q.append((dx,dy,0))
				else:
					q.append((dx,dy,d+1))
	return a-1
for i in range(W):
	for j in range(H):
		if m[j][i]=='X':
			Bfs((i,j))
			break
	else:
		continue
	break
print(bfs((i,j,0)))
