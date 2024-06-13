import sys
input=sys.stdin.readline
D=1000
N,B=map(int,input().split())
tmp=[list(map(lambda x:int(x)%1000,input().split())) for _ in range(N)]
def mul(a,b):
	mat=[[0]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				mat[i][j]+=a[i][k] * b[k][j]
			mat[i][j]%=D
	return mat
rst=[[0]*N for _ in range(N)]
for x in range(N):rst[x][x]=1
while B:
	if B%2==1:
		rst=mul(rst,tmp)
	tmp=mul(tmp,tmp)
	B>>=1
for R in rst:print(*R)
