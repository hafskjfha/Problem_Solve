import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
miro=[list(input().strip()) for _ in range(N)]
def bfs():
	q = deque([(0,0,1)])	
	while q:
		x,y,di=q.popleft()
		if miro[y][x] == '2':
			continue
		miro[y][x] = '2'
		if (x,y) == (M-1,N-1):
			return di
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0 <= dx < M and 0 <= dy < N and miro[dy][dx] == '1':
				q.append((dx,dy,di+1))
	return di
print(bfs())
