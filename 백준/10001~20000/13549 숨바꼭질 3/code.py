from collections import deque
N,K=map(int,input().split())
v=[0]*100001
def bfs():
	q=deque([(N,0)])
	while q:
		x,d=q.popleft()
		if v[x]:continue
		if x==K:return d
		v[x]=1
		for dx in (x*2,x-1,x+1):
			if 0<=dx<100001 and not v[dx]:
				if dx!=x*2:
					q.append((dx,d+1))
				else:
					q.append((dx,d))
print(bfs())
