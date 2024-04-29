import sys
input=sys.stdin.readline
N = int(input())
l = set(input().strip().split())
M = int(input())
y = input().strip().split()
for s in y:
	if s in l: print(1)
	else:	print(0)
