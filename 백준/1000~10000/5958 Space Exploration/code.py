import sys
from collections import deque
input=sys.stdin.readline
N,c=int(input()),0
m=[list(input().strip()) for _ in range(N)]
def bfs(A,B):
	q=deque([(A,B)])
	while q:
		x,y=q.popleft()
		if m[y][x]=='@':
			continue
		m[y][x]='@'
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<N and m[dy][dx]=='*':
				q.append((dx,dy))
for i in range(N):
	for j in range(N):
		if m[i][j]=='*':
			bfs(j,i)
			c+=1
print(c)
