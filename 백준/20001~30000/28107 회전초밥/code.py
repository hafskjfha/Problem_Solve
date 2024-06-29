import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
k=[[]for _ in range(200001)]
E=[0]*N
for i in range(N):
	O=[*map(int,input().split())][1:]
	for n in O:
		heapq.heappush(k[n],i)
B=[*map(int,input().split())]
for b in B:
	if k[b]:
		E[heapq.heappop(k[b])]+=1
print(*E,sep=' ')
