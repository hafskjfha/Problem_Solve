from collections import deque
N,M,I,J=map(int,input().split())
f=[[0]*N for _ in range(M)]
def bfs():
	q=deque([(0,-1,0)])
	while q:
		x,y,d=q.popleft()
		if f[y][x]==2:
			continue
		if (x,y)==(I-1,-J):
			return d
		f[y][x]=2
		for dx,dy in [(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2)]:
			if 0<=dx<N and -M<=dy<0 and f[dy][dx]==0:
				q.append((dx,dy,d+1))
	return "NEVAR"
print(bfs())
