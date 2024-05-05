import sys
from collections import deque
input=sys.stdin.readline
def bfs(S):
	q=deque([S])
	while q:
		x,y,z,di=q.popleft()
		if m[z][y][x]==5:
			continue
		if m[z][y][x]=='E':
			return di
		m[z][y][x]=5
		for dx,dy,dz in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
			if 0<=dx<C and 0<=dy<R and 0<=dz<L and (m[dz][dy][dx]=='.' or m[dz][dy][dx]=='E') :
				q.append((dx,dy,dz,di+1))
	return False
while 1:
	L,R,C=map(int,input().split())
	if (L,R,C)==(0,0,0):
		break
	m=[]
	for _ in range(L):
		p=[]
		for _ in range(R):
			p.append(list(input().strip()))
		m.append(p)
		input()
	for k in range(L):
		for i in range(R):
			for j in range(C):
				if m[k][j][i]=='S':
					a=bfs((i,j,k,0))
					break
			else:
				continue
			break
		else:
			continue
		break
	if a==False:
		print('Trapped!')
	else:
		print(f'Escaped in {a} minute(s).')
