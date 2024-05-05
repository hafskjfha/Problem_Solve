import sys
from collections import deque
input=sys.stdin.readline
M,N,H=map(int,input().split())
b,p=[],[]
for _ in range(H):
	r=[]
	for _ in range(N):
		r.append(list(map(int,input().split())))
	b.append(r)
def bfs(S):
	q,a=deque(S),0
	while q:
		x,y,z,di=q.popleft()
		if b[z][y][x]==2:
			continue
		b[z][y][x],a=2,max(a,di)
		for dx,dy,dz in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z-1),(x,y,z+1)]:
			if 0<=dx<M and 0<=dy<N and 0<=dz<H and b[dz][dy][dx]==0:
				q.append((dx,dy,dz,di+1))
	if a==0:
		return 0
	return a
for k in range(H):
	for i in range(M):
		for j in range(N):
			if b[k][j][i]==1:
				p.append((i,j,k,0))
if not p:
	print(-1)
	sys.exit()
e=bfs(p)
if e==0:
	print(0)
else:
	for k in range(H):
		for i in range(M):
			for j in range(N):
				if b[k][j][i]==0:
					print(-1)
					sys.exit()
	print(e)
