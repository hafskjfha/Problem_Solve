import sys
from collections import deque
input = sys.stdin.readline
de = deque()
N = int(input())
def de_notemp():
	if de:
		return True
	else:
		return False
for _ in range(N):
	cmd = tuple(map(int,input().split()))
	if cmd[0] == 1:
		de.appendleft(cmd[1])
	elif cmd[0] == 2:
		de.append(cmd[1])
	elif cmd[0] == 3:
		if de_notemp():
			print(de.popleft())
		else:
			print(-1)
	elif cmd[0] == 4:
		if de_notemp():
			print(de.pop())
		else:
			print(-1)
	elif cmd[0] == 5:
		print(len(de))
	elif cmd[0] == 6:
		if de_notemp():
			print(0)
		else:
			print(1)
	elif cmd[0] == 7:
		if de_notemp():
			print(de[0])
		else:
			print(-1)
	elif cmd[0] == 8:
		if de_notemp():
			print(de[-1])
		else:
			print(-1)
