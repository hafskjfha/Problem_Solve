import sys
INF=float('inf')
input=sys.stdin.readline
N,M=map(int,input().split())
gr=[[INF]*(N)for _ in range(N)]
for i in range(N):gr[i][i]=0
for _ in range(M):
	a,b,t=map(int,input().split())
	gr[a-1][b-1]=min(gr[a-1][b-1],t)
def floyd():
	for i in range(N):
		for j in range(N):
			for k in range(N):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
floyd()
K=int(input())
C=sorted([*map(int,input().split())])
Xl=[[INF]*(N) for _ in range(N)]
for i in C:
    for j in range(N):
        Xl[i-1][j]=gr[i-1][j]+gr[j][i-1]
A=[INF]*N
X=0
for i in range(N):
    s=0
    for j in C:
        s=max(s,Xl[j-1][i])
    A[i]=s
D=min(A)
for i in range(N):
    if A[i]==D:
        print(i+1,end=' ')
    
