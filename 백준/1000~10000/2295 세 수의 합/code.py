def main():
	input=open(0).readline
	N=int(input())
	A=sorted([int(input())for _ in range(N)])
	K=set()
	for i in A:
		for j in A:
			K.add(i+j)
	for i in range(N-1,-1,-1):
		for j in range(i+1):
			if A[i]-A[j] in K:
				print(A[i])
				return
main()
