import sys
from collections import deque
input=sys.stdin.readline
while True:
	N = input().strip()	
	if N == '0':
		break
	de = deque(list(N))
	dde=[]
	if len(N) ==1:
		print("yes")
	else:
		for _ in range(len(N)):
			dde.append(de.pop())
		b = ''.join(dde)
		if N ==b :
			print("yes")
		else:
			print("no")
