from itertools import combinations
from collections import deque
from copy import deepcopy
N,M=map(int,input().split())
S=[]
va=[]
A=0
for i in range(N):
	tmp=list(map(int,input().split()))
	for j in range(M):
		if tmp[j]==2:
			va.append((j,i))
	S.append(tmp)
def bfs(S):
	global A
	si=deepcopy(S)
	q=deque(va)
	while q:
		x,y=q.popleft()
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<M and 0<=dy<N and si[dy][dx]==0:
				q.append((dx,dy))
				si[dy][dx]=2
	W=0
	for i in range(M):
		for j in range(N):
			if si[j][i]==0:
				W+=1
	return max(A,W)
coordinates = [(x, y) for x in range(M) for y in range(N)]
combs = list(combinations(coordinates, 3))
for b1,b2,b3 in combs:
	x1,y1,x2,y2,x3,y3=b1[0],b1[1],b2[0],b2[1],b3[0],b3[1]
	if S[y1][x1]==0 and S[y2][x2]==0 and S[y3][x3]==0:
		S[y1][x1]=1
		S[y2][x2]=1
		S[y3][x3]=1
		A=bfs(S)
		S[y1][x1]=0
		S[y2][x2]=0
		S[y3][x3]=0
print(A)
