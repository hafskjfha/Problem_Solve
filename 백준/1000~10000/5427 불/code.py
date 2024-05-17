import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
def bfs(S):
	q,v=deque(S),[[0]*W for _ in range(H)]
	while q:
		x,y,d,info=q.popleft()
		if v[y][x]:continue
		if info=='*':m[y][x]='*'
		v[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and not v[dy][dx]:
				if info=='*':
					if m[dy][dx] in ('.','@'):
						q.append((dx,dy,d+1,'*'))
						m[dy][dx]='N'
				if info=='@':
					if m[dy][dx]=='.':
						q.append((dx,dy,d+1,'@'))
			elif (0>dx or dx>=W or 0>dy or dy>=H):
				if info=='@':
					return d
	return 'IMPOSSIBLE'
for _ in range(T):
	W,H=map(int,input().split())
	m,o=[],[]
	for j in range(H):
		l=list(input().strip())
		for i in range(W):
			if l[i]=='@':
				k=(i,j,1,'@')
			elif l[i]=='*':
				o.append((i,j,1,'*'))
		m.append(l)
	print(bfs(o+[k]))
