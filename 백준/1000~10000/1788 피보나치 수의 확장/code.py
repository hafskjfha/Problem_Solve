import sys
import math
input=sys.stdin.readline
N=int(input())
dp={-2:-1,-1:1,0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21}
if N==0:
	print(0,0,sep='\n')
elif N > 0:
	for i in range(9,N+1):
		dp[i] = (dp[i-1]+dp[i-2])%1000000000
	print(1)
	print(dp[N])
elif N < 0:
	for i in range(-1,N,-1):
		dp[i-2] = int(math.fmod((dp[i] - dp[i-1]), 1000000000))
	if dp[N] < 0:
		print(-1)
		print(abs(dp[N]))
	else:
		print(1)
		print(abs(dp[N]))
