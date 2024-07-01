import sys
input=sys.stdin.readline
c={}
for _ in range(int(input())-1):
        A,B=input().strip().split()
        c[A]=B
def ff(C,D):
        t=C
        while t:
                if (t:=c.get(t,0))==D:return 1
        t=D
        while t:
                if (t:=c.get(t,0))==C:return 1
        return 0
print(ff(*input().strip().split()))