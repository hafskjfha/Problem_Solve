def mul(a,b,p):
	mat=[[0,0],[0,0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				mat[i][j]+=a[i][k] * b[k][j]
			mat[i][j]%=p
	return mat
def su(a,r,n,p):
	rst=[[1,0],[0,1]]
	tmp=[[r,0],[a,1]]
	while n:
		if n%2:
			rst=mul(rst,tmp,p)
		tmp=mul(tmp,tmp,p)
		n>>=1
	return rst[1][0]
print(su(*map(int,input().split())))
