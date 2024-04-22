import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
de = deque(list(range(1,N+1)))
fi = list(map(int,input().split()))
c=0
for i in fi:
	if i == de[0]:
		de.popleft()
	else:
		while True:
			hf = len(de)//2
			if de[0] == i:
				de.popleft()
				break
			if de.index(i) <= hf:
				de.append(de.popleft())
				c+=1
			else:
				de.appendleft(de.pop())
				c+=1
		
print(c)
