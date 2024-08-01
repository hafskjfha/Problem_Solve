import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
def bfs(sx,sy):
	q=deque([(sx,sy)])
	while q:
		x,y=q.popleft()
		if f[y][x]=='@':
			continue
		f[y][x]='@'
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and f[dy][dx]=='#':
				q.append((dx,dy))
for _ in range(T):
	H,W=map(int,input().split())
	f,c=[list(input().strip()) for _ in range(H)],0
	for i in range(W):
		for j in range(H):
			if f[j][i]=='#':
				bfs(i,j)
				c+=1
	print(c)
