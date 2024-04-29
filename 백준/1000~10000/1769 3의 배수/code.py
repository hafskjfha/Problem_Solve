N = input()
j = list(map(int,N))
q = 0
o = sum(j)
if len(str(o)) == 1:
	if o % 3 == 0:
		print(0)
		print('YES')
	else:
		print(0)
		print('NO')
else:
	q += 1
	while True:
		u = [int(a) for a in str(o)]
		j = sum(u)
		q += 1
		if len(str(j)) == 1:
			if j % 3 == 0:
				print(q)
				print('YES')
				break
			else:
				print(q)
				print('NO')
				break
		else:
			o = j
