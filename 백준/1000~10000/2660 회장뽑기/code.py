import sys
INF=float('inf')
input=sys.stdin.readline
N=int(input())
gr=[[INF]*(N)for _ in range(N)]
for i in range(N):gr[i][i]=0
while 1:
	a,b=map(int,input().split())
	if (a,b)==(-1,-1):break
	gr[a-1][b-1]=1
	gr[b-1][a-1]=1
def floyd():
	for i in range(N):
		for j in range(N):
			for k in range(N):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
floyd()
P={}
i=1
for L in gr:
	try:
		P[max(L)].append(i)
		i+=1
	except:
		P[max(L)]=[i]
		i+=1
print(min(P.keys()),len(P[min(P.keys())]))
print(*P[min(P.keys())])
