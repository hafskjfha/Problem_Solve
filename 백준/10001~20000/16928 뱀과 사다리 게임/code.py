import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
B,vI={},[0]*101
for _ in range(N+M):
	x,y=map(int,input().split())
	B[x]=y
def bfs():
	q=deque([(1,0)])
	while q:
		x,c=q.popleft()
		if vI[x]:continue
		vI[x]=1
		for delta in range(6,0,-1):
			dx=x+delta
			if dx>=100:
				return c+1
			else:
				ddx=B.get(dx,False)
				if ddx and not vI[ddx] :
					q.append((ddx,c+1))
				elif not ddx and not vI[dx]:
					q.append((dx,c+1))
print(bfs())
