import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
	li.append(input().strip())
def sf(x):
	c = 0
	nu = ['1','2','3','4','5','6','7','8','9','0']
	for s in x:
		if s in nu:
			c += int(s)
	return c
sli = sorted(li,key=lambda x:(len(x),sf(x),x))
for j in sli:
	print(j)
