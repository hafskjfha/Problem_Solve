import sys
from collections import deque
input=sys.stdin.readline
M,N,T=map(int,input().split())
def bfs():
	q,a=deque([(0,0,0)]),float('inf')
	while q:
		x,y,d=q.popleft()
		if m[y][x]==9:continue
		if (x,y)==(N-1,M-1):
			a=min(a,d)
			return a
		if m[y][x]==2:
			d+=(N-1-x)+(M-1-y)
			if d>T:continue
			a=min(a,d)
			continue
		m[y][x]=9
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<M and m[dy][dx] not in(1,9) and d+1<=T:q.append((dx,dy,d+1))
	if a!=float('inf'):return a
	return 'Fail'
m=[list(map(int,input().split())) for _ in range(M)]
print(bfs())
