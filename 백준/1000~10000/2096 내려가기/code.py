#pypy3
import sys
input=sys.stdin.readline
N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
def P():
	a,b,c=M[0][0],M[0][1],M[0][2]
	for i in range(N-1):
		d,e,f=0,0,0
		j=i+1
		d=max(d,a+M[j][0],b+M[j][0])
		e=max(e,a+M[j][1],b+M[j][1],c+M[j][1])
		f=max(f,b+M[j][2],c+M[j][2])
		a,b,c=d,e,f
	return max(a,b,c)
def O():
	a,b,c=M[0][0],M[0][1],M[0][2]
	for i in range(N-1):
		d,e,f=float('inf'),float('inf'),float('inf')
		j=i+1
		d=min(d,a+M[j][0],b+M[j][0])
		e=min(e,a+M[j][1],b+M[j][1],c+M[j][1])
		f=min(f,b+M[j][2],c+M[j][2])
		a,b,c=d,e,f
	return min(a,b,c)
	
print(P(),O())
