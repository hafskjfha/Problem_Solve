import sys
from collections import deque
input=sys.stdin.readline
def bfs(S,v):
	q=deque([S])
	while q:
		x,y,d=q.popleft()
		if v[y][x]==4:continue
		if (x,y)==(W*2-2,H*2-2):return d+1
		v[y][x]=4
		if 0<=x+1<(W*2-1) and 0<=y<(H*2-1) and v[y][x+1]==0:
			q.append((x+2,y,d+1))
		if 0<=x-1<(W*2-1) and 0<=y<(H*2-1) and v[y][x-1]==0:
			q.append((x-2,y,d+1))
		if 0<=x<(W*2-1) and 0<=y+1<(H*2-1) and v[y+1][x]==0:
			q.append((x,y+2,d+1))
		if 0<=x<(W*2-1) and 0<=y-1<(H*2-1) and v[y-1][x]==0:
			q.append((x,y-2,d+1))
	return 0
while 1:
	W,H=map(int,input().split())
	if (W,H)==(0,0):
		break
	v,s,o=[['']*(W*2-1) for _ in range(H*2-1)],0,0
	m=[list(input()) for _ in range(H*2-1)]
	for i in m:
		o=0
		for j in i:
			if j=='0':
				v[s][o]=0
			elif j=='1':
				v[s][o]=1
			o+=1
		s+=1
	print((bfs((0,0,0),v)))
	
