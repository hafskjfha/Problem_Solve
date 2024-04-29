import sys
input=sys.stdin.readline
N,M =map(int,input().split())
col={}
nums={'1','2','3','4','5','6','7','8','9','0'}
i=0
for _ in range(N):
	i += 1	
	p = input().strip()
	col[str(i)] = p
	col[p] = i
for _ in range(M):
	a = input().strip()
	for j in nums:
		if j in a:
			a = a
			print(col[a])
			break
	else:
		a = a
		print(col[a])
