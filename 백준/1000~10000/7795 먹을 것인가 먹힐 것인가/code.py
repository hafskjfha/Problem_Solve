from bisect import bisect_left
input=open(0).readline
for _ in range(int(input())):
	n,m=map(int,input().split())
	a=[*map(int,input().split())]
	b=sorted([*map(int,input().split())])
	s=0
	for x in a:
		i=bisect_left(b,x)
		s+=i
	print(s)
