import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
dosi = [list(map(int, input().split())) for _ in range(M)]
def bfs():
	q = deque([(0,0)])
	while q:
		x,y = q.popleft()
		if dosi[y][x] == 2:
			continue
		if (x,y) == (N-1,M-1):
			return 'Yes'
		dosi[y][x] = 2
		for dx,dy in [(0,1),(1,0)]:
			nx,ny=x+dx,y+dy
			if nx<N and ny<M and dosi[ny][nx] == 1:
				q.append((nx,ny))
	return 'No'
print(bfs())
