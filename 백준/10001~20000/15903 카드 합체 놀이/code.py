import heapq
N,M=map(int,input().split())
h=[]
A=list(map(int,input().split()))
for a in A:heapq.heappush(h,a)
for _ in range(M):
	x=heapq.heappop(h)
	y=heapq.heappop(h)
	heapq.heappush(h,x+y)
	heapq.heappush(h,x+y)
print(sum(h))
