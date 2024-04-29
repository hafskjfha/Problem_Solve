import sys,math
input = sys.stdin.readline

dp = [1 for _ in range(1000000+1)]
floor = math.floor
for i in range(1,1000001):
	a,b,c= floor(i - i**0.5) , floor(math.log(i)) , floor(i * (math.sin(i))**2)
	dp[i] = (dp[a] + dp[b] + dp[c]) % 1000000
while True:
	n = int(input())
	if n == -1:
		break
	print(dp[n])
