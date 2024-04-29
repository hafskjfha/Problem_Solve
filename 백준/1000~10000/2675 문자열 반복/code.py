import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
	k=list(map(str,input().strip().split()))
  X,S=int(k[0]),list(k[1])
	for c in S:
		print(c*X,end="")
	print()

	
