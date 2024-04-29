import sys
from collections import deque
input=sys.stdin.readline
N = int(input())
for _ in range(N):
	j = 1
  y = list(map(int,input().split()))
	u = list(map(int,input().split()))
	i = y[1]
	de = deque(u)
	while True:
		ma = max(de)
		if de[0] != ma:
			de.append(de.popleft())
			i -= 1
			if i < 0:
				i = len(de)-1
		else:
			de.popleft()
			i -= 1
			if i < 0:
				print(j)
				break
			j += 1

			
