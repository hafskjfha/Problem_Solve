import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
lakes=[list(input().strip()) for _ in range(N)]
def bfs(sx,sy):
	a,q=0,deque([(sx,sy)])
	while q:
		x,y=q.popleft()
		if lakes[y][x]=='2':
			continue
		lakes[y][x]='2'
		a+=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<M and 0<=dy<N and lakes[dy][dx]=='1':
				q.append((dx,dy))
	return a
p,l=[],0
for i in range(M):
	for j in range(N):
		if lakes[j][i] == '1':
			p.append(bfs(i,j))
			l+=1
print(l)
print(*(sorted(p)))
