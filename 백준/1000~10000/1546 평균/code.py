import sys
input=sys.stdin.readline
N = int(input())
s = list(map(int,input().split()))
M = max(s)
S = []
for r in s:
	S.append(r/M*100)
print(sum(S)/N)
