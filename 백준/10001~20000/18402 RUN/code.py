import sys,heapq
input=sys.stdin.readline
N=int(input())
E=int(input())
T=int(input())
M=int(input())
eg,d=[[]for _ in range(N+1)],[float('inf')]*(N+1)
for i in range(M):
	a,b,w=map(int,input().split())
	eg[b].append([w,a])
def dijkstra(K):
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]!=w:continue
		for nw,nv in eg[v]:
			if d[nv]>w+nw:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
dijkstra(E)
c=0
for j in range(1,N+1):
	c+=1 if d[j]<=T else 0
print(c)
