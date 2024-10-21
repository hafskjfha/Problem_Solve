N=int(input())
dp=[[0]*10 for _ in range(N+1)]
for i in range(1,N+1):
	for j in range(10):
		if j==0:
			dp[i][0]=1
			continue
		dp[i][j]=(dp[i-1][j]+dp[i][j-1])%10007
print(sum(dp[N])%10007)
