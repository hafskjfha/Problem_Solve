import sys
input=sys.stdin.readline
N,M=map(int,input().split())
gr=[[0]*(N+1)]
for _ in range(N):gr.append([0]+list(map(int,input().split())))
def floyd():
	for i in range(1,N+1):
		for j in range(1,N+1):
			for k in range(1,N+1):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
floyd()
for _ in range(M):
	A,B,C=map(int,input().split())
	print("Enjoy other party")if gr[A][B]<=C else print("Stay here")
