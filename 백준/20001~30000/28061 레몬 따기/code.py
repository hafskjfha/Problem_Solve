N=int(input())
A=[*map(int,input().split())]
r=0
for i in range(N):
	r=max(A[i]-(N-i),r)
print(r)
