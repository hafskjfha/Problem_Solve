import sys
input=sys.stdin.readline
N = int(input())
u = []
for _ in range(N):
	d = tuple(map(int,input().split()))
  u.append(d)
u.sort(key=lambda x:(x[0],x[1]))
for w in u:
	print(w[0],w[1])
