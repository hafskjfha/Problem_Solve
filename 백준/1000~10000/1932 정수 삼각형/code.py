import sys
input=sys.stdin.readline
N=int(input())
dp=[0]*N
k=2
M=list(map(int,input().split()))
dp[0]=M[0]
def p(M,dp,k):
	tmp=[0]*N
	tmp[0]=M[0]+dp[0]
	for j in range(1,k-1):
		tmp[j]=max(dp[j]+M[j],dp[j-1]+M[j])
	tmp[k-1]=M[-1]+dp[k-2]
	return tmp
	
for _ in range(N-1):
	M=list(map(int,input().split()))
	dp=p(M,dp,k)
	k+=1
print(max(dp))
