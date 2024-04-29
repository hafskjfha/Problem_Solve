import sys
input=sys.stdin.readline
N=int(input())
for _ in range(N):
	T=list(map(int,input().split()));	j=T[1:]
	h=None
	c=0
	for i in j:
		if i==j[0]:
			h=i
			c+=1
		else:
			if i==h:
				c+=1
			else:
				c-=1
				if c==0:
					h=i
					c=1
	if j.count(h) > len(j)//2:
		print(h)
	else:
		print("SYJKGW")
