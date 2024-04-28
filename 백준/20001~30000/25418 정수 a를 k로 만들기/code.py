import sys
input = sys.stdin.readline
A,K = map(int,input().split())
c=0
while K>A:
	if K%2==0:
		if K//2 < A:
			break
		K //= 2
		c += 1
	else:
		K -= 1
		c += 1
if K>A:
	c += K-A
print(c)
