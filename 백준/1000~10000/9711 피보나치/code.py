import sys
input = sys.stdin.readline
T = int(input())
dp={1:1,2:1}
for i in range(3,10001):
	dp[i] = (dp[i-1]+dp[i-2])
for t in range(1,T+1):
	P, Q = map(int,input().split())
	print(f"Case #{t}: {dp[P]%Q}")
