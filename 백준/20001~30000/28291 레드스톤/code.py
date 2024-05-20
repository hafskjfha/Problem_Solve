import sys
from collections import deque
input=sys.stdin.readline
W,H=map(int,input().split())
N=int(input())
m,v,rb,rl=[[0]*W for _ in range(H)],[[0]*W for _ in range(H)],[],[]
for _ in range(N):
	o=tuple(input().strip().split(' '))
	a,b=int(o[1]),int(o[2])
	if o[0]=='redstone_block':
		m[b][a]='rb'
		rb.append((a,b))
	elif o[0]=='redstone_dust':
		m[b][a]='rd'
	else:
		m[b][a]='rl'
		rl.append((a,b))

def bfs(sx,sy):
	q=deque([(sx,sy,16)])
	while q:
		x,y,p=q.popleft()
		if v[y][x]>=p:continue
		v[y][x]=p
		if m[y][x]=='rl':continue
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx] in ('rd','rl'):
				q.append((dx,dy,p-1))
for x,y in rb:
	bfs(x,y)
	for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
		if 0<=dx<W and 0<=dy<H:v[dy][dx]=15
for a,b in rl:
	if not v[b][a]:
		print('failed')
		sys.exit()
print('success')
	
