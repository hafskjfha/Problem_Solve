import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
eg,d=[[]for _ in range(N)],[float('inf')]*N
A=[*map(int,input().split())]
A[-1]=0
for i in range(M):
	a,b,t=map(int,input().split())
	if A[a]==0 and A[b]==0:
		eg[a].append([t,b])
		eg[b].append([t,a])
def dijkstra():
	d[0]=0
	heap=[[0,0]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
dijkstra()
print(-1)if d[-1]==float('inf')else print(d[-1])
