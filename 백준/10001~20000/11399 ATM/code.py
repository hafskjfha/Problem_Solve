import sys
input=sys.stdin.readline
N=int(input())
y=[]
i=1
a=0
c=0
j = list(map(int,input().split()))
for p in j:
	y.append((i,p))
  i+=1
y.sort(key=lambda x:x[1])
for l in y:
	b = a+l[1]
	a=b
	c=c+a
print(c)
