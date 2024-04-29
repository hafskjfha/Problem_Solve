import sys
input=sys.stdin.readline
it=[0,1,2,3,4,5,6,7,8,9]
k=[]
for _ in range(3):
	k.append(int(input()))
j=str(k[0]*k[1]*k[2])
for i in it:
	i=str(i)
	print(j.count(i))

	
