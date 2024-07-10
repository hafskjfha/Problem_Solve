import sys,heapq
input=sys.stdin.readline
N,P,C,M=map(int,input().split())
eg,d=[[]for _ in range(N+1)],[float('inf')]*(N+1)
for i in range(P):
	F1,F2,T=map(int,input().split())
	eg[F1].append([T,F2])
	eg[F2].append([T,F1])
cd={i:[]for i in range(1,N+1)}
for i in range(1,C+1):
	cd[int(input())].append(i)
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
dijkstra(1)
A=[]
for j in range(1,N+1):
	if j !=float('inf') and d[j]<=M:
		if (k:=cd.get(j,False)):
			A.extend(k)
print(len(A))
print(*sorted(A),sep='\n')
