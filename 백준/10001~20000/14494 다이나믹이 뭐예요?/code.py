import sys
input = sys.stdin.readline
N, M = map(int, input().split())
DP = [[0] * (N + 1) for _ in range(M + 1)]
DP[1][1] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 and j == 1:
            continue
        DP[j][i] = (DP[j][i - 1] + DP[j - 1][i] + DP[j - 1][i - 1]) % 1000000007
        
print(DP[M][N])
