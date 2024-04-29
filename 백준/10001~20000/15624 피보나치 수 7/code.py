import sys
input=sys.stdin.readline
N=int(input())
dp={0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21}
for i in range(9,N+1):
	dp[i] = (dp[i-1]+dp[i-2])%1000000007
print(dp[N])
