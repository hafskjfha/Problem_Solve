input=open(0).readline
def sol(A,N,T):
	c=0
	for i in A:
		c+=i//T
	return 0 if c<N else 1
	
def main():
	K,N=map(int,input().split())
	A=sorted([int(input())for _ in range(K)])
	start,end=1,A[-1]
	while start<=end:
		mid=(start+end)//2
		if sol(A,N,mid):
			ans=mid
			start=mid+1
		else:
			end=mid-1
	print(ans)

main()
