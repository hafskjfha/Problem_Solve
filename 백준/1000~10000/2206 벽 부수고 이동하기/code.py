import sys
from collections import deque
N,M=map(int,input().split())
W=[list(input().strip()) for _ in range(N)]
def bfs(S,P):
	q,v=deque([S]),[[0]*M for _ in range(N)]
	while q:
		x,y,d,b=q.popleft() 
		if (x,y)==(M-1,N-1) and P==0:return d
		elif (x,y)==(0,0) and P==1:return d
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<M and 0<=dy<N and (dx,dy) and not v[dy][dx]:
				t=W[dy][dx]
				if t=="0":
					q.append((dx,dy,d+1,b))
					v[dy][dx]=1
				elif t=="1" and not b:
					q.append((dx,dy,d+1,True))
					v[dy][dx]=1
	return -1
a,b=bfs((0,0,1,False),0),bfs((M-1,N-1,1,False),1)
if a==-1 and b==-1:
	print(-1)
elif -1 in (a,b):
	print(max(a,b))
else:
	print(min(a,b))
