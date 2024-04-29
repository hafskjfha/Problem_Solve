kk = input()
p = 0
l = ['dz=','lj','nj','c=','c-','d-','z=','s=']
for s in l:
	p += kk.count(s)
	kk = kk.replace(s,' ')
a = kk.replace(' ','')
p += len(a)
print(p)                                                   
