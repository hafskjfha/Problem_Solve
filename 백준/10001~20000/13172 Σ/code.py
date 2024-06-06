import sys,math
from functools import reduce
input=sys.stdin.readline
S,N,W,D=[],[],[],int(1e9+7)
rm=lambda x:pow(x,D-2,D)
LCM=lambda x,y:abs(x*y)//math.gcd(x,y)
aLCM=lambda x:reduce(LCM,x)
for _ in range(int(input())):
	b,a=map(int,input().split())
	S.append(a)
	N.append(b)
c=aLCM(N)
for i in range(len(S)):
	W.append(c//N[i]*S[i])
Q=sum(W)
print(Q//c)if not Q%c else print(Q*rm(c)%D)
