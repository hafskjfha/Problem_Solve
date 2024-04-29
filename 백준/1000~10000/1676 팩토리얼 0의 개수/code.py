import math
N = int(input())
r = list(str(math.factorial(N)))
p = 0
if r[-1] != '0':
	print(0)
else:
	while True:
		if r[-1] != '0':
			print(p)
			break
		else:
			r.pop()
			p += 1
