import math
def mul(a,b):
	mat=[[0,0],[0,0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				mat[i][j]+=a[i][k] * b[k][j]
			mat[i][j]%=1000000007
	return mat
def fibo(T):
	rst=[[1,0],[0,1]]
	tmp=[[1,1],[1,0]]
	while T:
		if T%2==1:
			rst=mul(rst,tmp)
		tmp=mul(tmp,tmp)
		T>>=1
	return rst[0][1]
for _ in range(int(input())):
	N,M=map(int,input().split())
	print(fibo(math.gcd(N,M)))
