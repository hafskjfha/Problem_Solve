import sys
input = sys.stdin.readline
M,N = map(int,input().split())
DP = [[0]*(N) for _ in range(M)]
miro = []
for _ in range(M):
	miro.append(list(map(int,input().split())))
DP[0][0] = miro[0][0]
for i in range(M):
	for j in range(N):
		if j+1 < N:
			DP[i][j+1] = max((DP[i][j] + miro[i][j+1]), DP[i][j+1])
		if i+1 < M:
			DP[i+1][j] = max((DP[i][j] + miro[i+1][j]), DP[i+1][j])
print(DP[M-1][N-1])
