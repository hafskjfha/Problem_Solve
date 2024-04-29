import sys
input = sys.stdin.readline
N = int(input())
sel = {}
for _ in range(N):
	book = input().strip()
	if book in sel:
		sel[book] += 1
	else:
		sel[book] = 1
nab = []
bes = sorted(sel.items(),key=lambda x:(x[1],x[0]),reverse=True)

for n,v in bes:
	if v == bes[0][1]:
		nab.append(n)
	else:
		break
nab.sort()
print(nab[0])
