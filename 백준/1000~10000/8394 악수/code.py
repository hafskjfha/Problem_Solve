import sys
input = sys.stdin.readline
N = int(input())#int(input())%60 피사노 주기
dp=[0]*(N+1)
if N==2:
	print(2)
	sys.exit()
elif N==3:
	print(3)
	sys.exit()
dp[2],dp[3]=2,3
for i in range(4,N+1):
	dp[i] = (dp[i-1] + dp[i-2])%10
print(dp[N])
