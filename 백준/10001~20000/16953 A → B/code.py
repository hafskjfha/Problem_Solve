# BFS식 풀이
from collections import deque
A,B=map(int,input().split())
def bfs():
	q,v=deque([(A,0)]),set()
	while q:
		x,c=q.popleft()
		if x==B:return c+1
		v.add(x)
		for dx in [x*2,x*10+1]:
			if dx<=B and dx not in v:
				q.append((dx,c+1))
	return -1
print(bfs())
