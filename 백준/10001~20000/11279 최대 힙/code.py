import sys
import heapq
input=sys.stdin.readline
N=int(input())
h=[]
for _ in range(N):
	p = int(input());	p = -1*p
	if p ==0:
		if len(h)==0:
			print(0)
		else:
			print(-1*heapq.heappop(h))
	else:
		heapq.heappush(h,p)
