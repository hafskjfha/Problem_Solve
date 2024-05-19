import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
v1,v2,m,A,B,RA,RB=[[0]*N for _ in range(N)],[[0]*N for _ in range(N)],[],{},{},0,0
for _ in range(N):
	o=input().strip().split()
	m.append([(o[i],int(o[i+1])) for i in range(0,N*2,2)])
def bfs(S,v,t):
	q,c,a=deque([S]),0,0
	while q:
		x,y,info=q.popleft()
		if v[y][x]:continue
		v[y][x]=1
		c+=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<N and not v[dy][dx] and m[dy][dx][t]==info :
				q.append((dx,dy,info))
	for i in range(c):
		a+=i
	return a
for i in range(N):
	for j in range(N):
		p=m[j][i]
		if not v1[j][i]:
			if p[0] in A:
				A[p[0]].append(bfs((i,j,p[0]),v1,0))
			else:
				A[p[0]]=[bfs((i,j,p[0]),v1,0)]
		if not v2[j][i]:
			if p[1] in B:
				B[p[1]].append(bfs((i,j,p[1]),v2,1))
			else:
				B[p[1]]=[bfs((i,j,p[1]),v2,1)]
for g,k in A.items():
	RA+=max(k)
for g,k in B.items():
	RB+=max(k)
print(RA,RB)
