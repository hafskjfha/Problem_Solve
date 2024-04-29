import sys
input=sys.stdin.readline
N = int(input())
for _ in range(N):
	h = input().strip()
  u = h
	for __ in range(len(h)):
		u = u.replace('()','')
	if len(u) == 0:
		print("YES")
	else:
		print("NO")
