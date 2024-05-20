import sys
from collections import deque
input=sys.stdin.readline
H,W=map(int,input().split())
m=[list(input().strip()) for _ in range(H)]
def bfs():
	q=deque([(0,0,[(1,1)])])
	while q:
		x,y,l=q.popleft()
		if m[y][x]==4:continue
		if (x,y)==(W-1,H-1):return l
		m[y][x]=4
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx] =='.':
				q.append((dx,dy,l+[(dy+1,dx+1)]))
for i in bfs():
	print(*i)
