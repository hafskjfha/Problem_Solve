from collections import deque

import sys
input=sys.stdin.readline
N = int(input())
de = deque([])
for _ in range(N):
	I = input().split()	
	if I[0] == 'push_front':
		de.appendleft(int(I[1]))
	elif I[0] == 'push_back':
		de.append(int(I[1]))
	elif I[0] == 'pop_front':
		if len(de) == 0:
			print(-1)
		else:
			print(de.popleft())
	elif I[0] == 'pop_back':
		if len(de) == 0:
			print(-1)
		else:
			print(de.pop())
	elif I[0] == 'size':
		print(len(de))
	elif I[0] == 'empty':
		if len(de)==0:
			print(1)
		else:
			print(0)
	elif I[0]=='front':
		if len(de)==0:
			print(-1)
		else:
			print(de[0])
	elif I[0] == 'back':
		if len(de)==0:
			print(-1)
		else:
			print(de[-1])
