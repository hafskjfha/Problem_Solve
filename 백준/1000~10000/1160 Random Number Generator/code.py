def mul(a,b,p):
	mat=[[0,0],[0,0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				mat[i][j]+=a[i][k]*b[k][j]
			mat[i][j]%=p
	return mat
def su(a,c,n,p):
	rst=[[1,0],[0,1]]
	tmp=[[a%p,0],[c%p,1]]
	while n:
		if n&1:
			rst=mul(rst,tmp,p)
		tmp=mul(tmp,tmp,p)
		n>>=1
	return rst
def main():
	m,a,c,X0,n,g=map(int,input().split())
	print(mul([[X0%m,1],[0,0]],su(a,c,n,m),m)[0][0]%g)
main()
