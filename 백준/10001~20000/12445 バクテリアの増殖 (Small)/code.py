y=[*open(0)]
for i in range(int(y[0])):
	a,b,c=map(int,y[i+1].split())
	if b>1:a**=a
	print(f"Case #{i+1}: {pow(a,a,c)}")
