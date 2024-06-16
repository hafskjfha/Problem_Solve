import sys
input=sys.stdin.readline
N,M=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(N)]
psum = [[0] * (N + 1) for _ in range(N + 1) ]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = mat[i - 1][j - 1]  + psum[i-1][j] + psum[i][j-1] - psum[i -1][j - 1]
A=[tuple(map(int,input().split())) for _ in range(M)]
for x1,y1,x2,y2 in A:
	an = psum[x2][y2]  + psum[x1 -1][y1 -1] - psum[x2][y1 - 1] - psum[x1 - 1][y2]
	print(an)
