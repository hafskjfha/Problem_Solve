import sys
input=sys.stdin.readline
c={}
for _ in range(int(input())-1):
	A,B=input().strip().split()
	c[A]=B
def ff(C,D):
	t=C
	while 1:
		if (t:=c.get(t,0))==0:break
		if t==D:return 1
	t=D
	while 1:
		if (t:=c.get(t,0))==0:break
		if t==C:return 1
	return 0
print(ff(*input().strip().split()))
