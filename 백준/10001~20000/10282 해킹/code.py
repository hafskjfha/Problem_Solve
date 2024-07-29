import sys,heapq
input=sys.stdin.readline
def dijkstra(K,n):
	d=[float('inf')]*(n+1)
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
	return d
for _ in range(int(input())):
	N,D,C=map(int,input().split())
	eg=[[]for _ in range(N+1)]
	for _ in range(D):
		a,b,s=map(int,input().split())
		eg[b].append([s,a])
	p,t=0,0
	A=dijkstra(C,N)
	for i in range(1,N+1):
		if A[i]!=float('inf'):
			p+=1
			t=max(A[i],t)
	print(p,t)
