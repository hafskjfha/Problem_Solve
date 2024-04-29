import sys
from collections import deque
input=sys.stdin.readline
N,M =map(int,input().split())
de = deque(range(1,N+1))
h = []
while de:
	for _ in range(M-1):		
		de.append(de.popleft())
	h.append(str(de.popleft()))
print('<'+', '.join(h)+'>')
