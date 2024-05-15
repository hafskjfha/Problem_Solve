from collections import deque
N,K=map(int,input().split())
v=[0]*100001
def bfs():
	if K<N:return f'{N-K}\n'+' '.join(map(str,range(N,K-1,-1)))
	q=deque([(N,0,[str(N)])])
	while q:
		x,d,l=q.popleft()
		if v[x]:continue
		if x==K:return f'{d}\n'+' '.join(l)
		v[x]=1
		for dx in (x-1,x+1,x*2):
			if 0<=dx<100001 and not v[dx]:
				q.append((dx,d+1,l+[str(dx)]))
print(bfs())
