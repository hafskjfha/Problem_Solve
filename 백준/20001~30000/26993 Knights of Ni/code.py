import sys
from collections import deque
input=sys.stdin.readline
W,H=map(int,input().split())
m,n=[],float('inf')
for _ in range(H):
	if W%40==0:b=W//40
	else:b=W//40+1
	f=[]
	for _ in range(b):
		f+=list(map(int,input().split()))
	m.append(f)
def bfs(S):
	global n
	q,e,vi=deque([S]),n,[[0]*W for _ in range(H)]
	while q:
		x,y,d=q.popleft()
		if vi[y][x]:continue
		if m[y][x]==4:
			e=min(e,bf((x,y,d),e))
			continue
		vi[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx] not in (1,3) and not vi[dy][dx] :
				q.append((dx,dy,d+1))
	return e
def bf(S,o):
	q,v=deque([S]),[[0]*W for _ in range(H)]
	while q:
		x,y,d=q.popleft()
		if v[y][x]:continue
		if m[y][x]==3:return d
		v[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]!=1 and not v[dy][dx] :
				if d+1>o:return n
				q.append((dx,dy,d+1))
for i in range(W):
	for j in range(H):
		if m[j][i]==2:
			break
	else:
		continue
	break
print(bfs((i,j,0)))
