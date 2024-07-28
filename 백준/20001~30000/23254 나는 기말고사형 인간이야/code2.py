import heapq
N,M=map(int,input().split())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
pq=[]
for i in range(M):
	heapq.heappush(pq,[-B[i],i])
S=sum(A)
N*=24
while N:
	try:
		b,i=pq[0]
		if -b+A[i]>100:
			heapq.heappop(pq)
			heapq.heappush(pq,[-(100-A[i]),i])
		elif -b+A[i]==100:
			heapq.heappop(pq)
			A[i]=100
			S+=-b
			N-=1
		else:
			A[i]+=-b
			S+=-b
			N-=1
	except:
		break
print(S)
