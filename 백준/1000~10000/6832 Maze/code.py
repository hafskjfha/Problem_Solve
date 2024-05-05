import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
def bfs():
	q=deque([(0,0,1)])
	while q:
		x,y,di=q.popleft()
		if m[y][x]==5:
			continue
		if (x,y)==(W-1,H-1):
			return di
		s=m[y][x]
		m[y][x]=5
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]!='*':
				if s=='+':
					q.append((dx,dy,di+1))
				elif s=='-' and dy==y:
					q.append((dx,dy,di+1))
				elif s=='|' and dx==x:
					q.append((dx,dy,di+1))
	return -1
for _ in range(T):
	H=int(input());W=int(input())
	m=[list(input().strip()) for _ in range(H)]
	print(bfs())
