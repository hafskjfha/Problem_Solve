import sys,heapq
input=sys.stdin.readline
N=int(input())
M=int(input())
eg,d=[[]for _ in range(N+1)],[float('inf')]*(N+1)
for i in range(M):
	u,v,w=map(int,input().split())
	eg[u].append([w,v])
K,T=map(int,input().split())
d[K]=0
h=[[0,K]]
while h:
	w,v=heapq.heappop(h)
	if d[v]!=w:continue
	for nw,nv in eg[v]:
		if d[nv]>w+nw:
			d[nv]=w+nw
			heapq.heappush(h,[d[nv],nv])
print(d[T])
