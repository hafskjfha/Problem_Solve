import sys
input=sys.stdin.readline
from collections import deque
T=int(input())
def bfs(S,E):
	q,v=deque([(S,[])]),[0]*10001
	while q:
		x,l=q.popleft()
		if x==E:return l
		if v[x]:continue
		v[x]=1
		dx=x*2
		if dx>9999:
			ddx=dx%10000
			if not v[ddx]:
				q.append((dx%10000,l+['D']))
		else:
			if not v[dx]:
				q.append((dx,l+['D']))
		dx=x-1
		if dx<0 and not v[9999]:
			q.append((9999,l+['S']))
		elif dx>=0 and not v[dx]:
			q.append((dx,l+['S']))
		dx=(x%1000)*10+x//1000
		if not v[dx]:
			q.append((dx,l+['L']))
		dx = (x%10)*1000+x//10
		if not v[dx]:
			q.append((dx,l+['R']))
		
for _ in range(T):
	A,B=map(int,input().split())
	print(*bfs(A,B),sep="")
