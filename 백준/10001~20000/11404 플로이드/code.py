import sys
INF=float('inf')
input=sys.stdin.readline
N=int(input())
M=int(input())
gr=[[INF]*(N+1)for _ in range(N+1)]
for i in range(1,N+1):gr[i][i]=0
for _ in range(M):
	a,b,c=map(int,input().split())
	gr[a][b]=min(gr[a][b],c)
def floyd():
	for i in range(1,N+1):
		for j in range(1,N+1):
			for k in range(1,N+1):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
floyd()
for i in range(1,N+1):
	for j in range(1,N+1):
		if (I:=gr[i][j])==INF:print(0,end=' ')
		else:print(I,end=' ')
	print()
