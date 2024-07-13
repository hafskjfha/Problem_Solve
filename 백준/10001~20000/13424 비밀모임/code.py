import sys
INF=float('inf')
input=sys.stdin.readline
def floyd(N,gr):
	for i in range(1,N+1):
		for j in range(1,N+1):
			for k in range(1,N+1):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
	return gr
def main():
	for _ in range(int(input())):
		N,M=map(int,input().split())
		gr=[[INF]*(N+1)for _ in range(N+1)]
		for i in range(1,N+1):gr[i][i]=0
		for _ in range(M):
			a,b,c=map(int,input().split())
			gr[a][b]=c
			gr[b][a]=c
		K=int(input())
		F=[*map(int,input().split())]
		A=floyd(N,gr)
		S=[0]*(N+1)
		S[0]=INF
		for i in range(1,N+1):
			k=0
			for j in F:
				k+=gr[i][j]
			S[i]=k
		v=min(S)
		for i in range(1,N+1):
			if S[i]==v:
				print(i)
				break
if __name__=='__main__':
	main()
