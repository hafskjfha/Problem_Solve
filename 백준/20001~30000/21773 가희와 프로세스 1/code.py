from heapq import heappush,heappop
import sys
input=sys.stdin.readline
push=heappush
pop=heappop
T,N=map(int,input().split())
pq=[]
for _ in range(N):
	A,B,C=map(int,input().split())
	push(pq,[-C,A,B])
for _ in range(T):
	try:
		c,a,b=pop(pq)
		print(a)
		b-=1
		if b:
			push(pq,[c+1,a,b])
	except:
		break