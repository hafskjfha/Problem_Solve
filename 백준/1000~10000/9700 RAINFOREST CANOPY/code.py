import sys
from collections import deque
input,p=sys.stdin.readline,1
def bfs(S):
	q=deque([S])
	while q:
		x,y=q.popleft()
		if m[y][x]==3:
			continue
		m[y][x]=3
		for dx,dy in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
			if 0<=dx<N and 0<=dy<N and m[dy][dx]=='1':
				q.append((dx,dy))
while 1:
	try:
		N,c=int(input()),0
		m=[list(input().strip()) for _ in range(N)]
		for i in range(N):
			for j in range(N):
				if m[j][i]=='1':
					bfs((i,j))
					c+=1
		print(f'Case #{p}: {c}');p+=1
	except:
		sys.exit()
