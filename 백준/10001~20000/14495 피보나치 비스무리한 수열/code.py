import sys
input=sys.stdin.readline
N=int(input())
dp={1:1,2:1,3:1}
for i in range(4,N+1):
	dp[i] = dp[i-1]+dp[i-3]
print(dp[N])
