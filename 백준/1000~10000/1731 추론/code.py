a=[*open(0)][1:]
d=int(a[1])-int(a[0])
r=int(a[1])//int(a[0])
if int(a[1])+d==int(a[2]):
	print(int(a[-1])+d)
else:
	print(int(a[-1])*r)
