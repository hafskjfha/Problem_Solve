import sys
input=sys.stdin.readline
N, M = map(int, input().split())
de=set()
bo=set()
for _ in range(N):
	s = input().strip()
        de.add(s)
for _ in range(M):
	s = input().strip()
	bo.add(s)
h = de & bo
h=sorted(h)
print(len(h))
for c in h:
	print(c)
