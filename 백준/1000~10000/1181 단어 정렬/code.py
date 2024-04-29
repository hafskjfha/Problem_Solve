import sys
g = int(sys.stdin.readline())
y = []
for _ in range(g):
	y.append(sys.stdin.readline().strip())
y = list(set(y))
y.sort()
y = sorted(y,key=len)
for s in y:
	print(s)
