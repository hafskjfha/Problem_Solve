import sys
input = sys.stdin.readline
nA,nB = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
cs = sorted(A - B)
if len(cs) == 0:
	print(0)
else:
	print(len(cs))
	print(" ".join(map(str,cs)))
