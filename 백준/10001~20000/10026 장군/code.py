import sys
from collections import deque
input=sys.stdin.readline
def bfs1(sx,sy):
	c,q=m[sy][sx],deque([(sx,sy)])
	while q:
		x,y=q.popleft()
		if h1[y][x]:
			continue
		h1[y][x]=True
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<N and m[dy][dx]==c:
				q.append((dx,dy))
	return 1
def bfs2(sx,sy):
	c,q=m[sy][sx],deque([(sx,sy)])
	if c=='R' or c=='G':
		c=('R','G')
	else:
		c=tuple(c)
	while q:
		x,y=q.popleft()
		if h2[y][x]:
			continue
		h2[y][x]=True
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<N and m[dy][dx] in c:
				q.append((dx,dy))
	return 1
N,a1,a2=int(input()),0,0
m=[list(input().strip()) for _ in range(N)]
h1,h2=[[False]*N for _ in range(N)],[[False]*N for _ in range(N)]
for i in range(N):
	for j in range(N):
		if not h1[j][i]:
			a1+=bfs1(i,j)
for i in range(N):
	for j in range(N):
		if not h2[j][i]:
			a2+=bfs2(i,j)
print(a1,a2)
