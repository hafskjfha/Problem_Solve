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
		b,i=heapq.heappop(pq)	
		t=(100-A[i])//-b
		if (100-A[i])%-b:
			heapq.heappush(pq,[-(100-A[i]--b*t),i])
		if t>N:
			t=N
		A[i]+=-b*t
		N-=t
		S+=-b*t
	except:
		break
print(S)
