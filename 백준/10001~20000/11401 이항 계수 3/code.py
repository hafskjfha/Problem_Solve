D=1000000007
def fac(n):
	if n==0:return 1
	t=1
	for i in range(2,n+1):
		t = (t*i)%D
	return t
N,K=map(int,input().split())
M=pow(fac(N-K)*fac(K),D-2,D)
print((fac(N)*M)%D)
