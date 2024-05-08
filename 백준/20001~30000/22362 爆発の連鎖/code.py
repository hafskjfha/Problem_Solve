import sys
from collections import deque
input=sys.stdin.readline
def bfs(s):
	q,v,c=deque([S]),[[0]*W for _ in range(H)],0
	while q:
		x,y=q.popleft()
		if not 0<=x<W or not 0<=y<H:continue
		if v[y][x]:continue
		v[y][x]=1
		if m[y][x]==1:
			c+=1
			for i in range(1,D+1):
				q.append((x-i,y))
				q.append((x+i,y))
				q.append((x,y-i))
				q.append((x,y+i))
	return c
while 1:
	W,H,N,D,B=map(int,input().split())
	if (W,H,N,D,B)==(0,0,0,0,0):break
	m=[[0]*W for _ in range(H)]
	for i in range(1,N+1):
		a,b=map(int,input().split())
		if i==B:S=(a-1,b-1)
		m[b-1][a-1]=1
	print(bfs(S))
