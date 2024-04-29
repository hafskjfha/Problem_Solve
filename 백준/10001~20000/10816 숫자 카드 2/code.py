import sys
from collections import Counter
input=sys.stdin.readline
N=int(input())
g=''
u = input().strip().split()
k=set(u)
d=Counter(u)
M=int(input())
y = input().strip().split()
for j in y:
	p = d.get(j)	
	if p != None:
		print(d[j],end=' ')
	else:
		print(0,end=' ')
