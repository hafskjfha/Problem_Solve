N,r,c=map(int,input().split())
def Z(K,c,r):
	if K<=1:
		if (c,r)==(0,0):return 0
		elif (c,r)==(1,0):return 1
		elif (c,r)==(0,1):return 2
		else:return 3
	T=K-1
	S=2**T
	if c<S and r<S:return Z(T,c,r)
	elif c>=S and r<S:return S*S+Z(T,c-S,r)
	elif c<S and r>=S:return 2*(S*S)+Z(T,c,r-S)
	elif c>=S and r>=S:return 3*(S*S)+Z(T,c-S,r-S)
print(Z(N,c,r))
