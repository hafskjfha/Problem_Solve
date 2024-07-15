#pypy
import sys
INF=float('inf')
def floyd(gr,N):
	for i in range(N):
		for j in range(N):
			for k in range(N):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
	return gr
def main():
    input=sys.stdin.readline
    N,M=map(int,input().split())
    gr=[[INF]*(N)for _ in range(N)]
    for i in range(N):gr[i][i]=0
    for _ in range(M):
	    a,b=map(int,input().split())
	    gr[a-1][b-1]=1
    floyd(gr,N)
    s=0
    for x in range(N):
        for y in range(N):
            if gr[y][x]==INF and gr[x][y]==INF:
                break
        else:
            s+=1
    print(s)
if __name__ == '__main__':
    main()
