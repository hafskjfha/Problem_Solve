D=1000000000
a,b=map(int,input().split())
def mul(a,b):
	mat=[[0,0],[0,0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				mat[i][j]+=a[i][k] * b[k][j]
			mat[i][j]%=D
	return mat
def fibo(N):
	rst=[[1,0],[0,1]]
	tmp=[[1,1],[1,0]]
	while N:
		if N%2==1:
			rst=mul(rst,tmp)
		tmp=mul(tmp,tmp)
		N>>=1
	return rst[0][1]
print((fibo(b+2)-fibo(a+1))%D)
