import sys
from collections import deque
input=sys.stdin.readline
N = int(input())
de = deque([])
for _ in range(N):
	p=int(input())	
	if p==0:
		de.pop()
	else:
		de.append(p)
print(sum(de))
