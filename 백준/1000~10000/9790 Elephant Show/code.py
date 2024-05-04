import sys
from collections import deque
input=sys.stdin.readline
def bfs(S):
	q,a=deque([(S)]),0
	while q:
		x,y=q.popleft()
		if m[y][x]==1:
			continue
		m[y][x]=1
		a+=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]=='.':
				q.append((dx,dy))
	return a
while 1:
	W,H=map(int,input().split())
	if (W,H)==(0,0):
		break
	m=[list(input().strip()) for _ in range(H)]
	for i in range(W):
		for j in range(H):
			if m[j][i]=='A':
				print(bfs((i,j)))
				break
