import sys
INF=float('inf')
def floyd(gr):
	for i in range(53):
		for j in range(53):
			for k in range(53):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
	return gr
def cc(c):
    if 'A'<=c<='Z':
        return ord(c) - ord('A')
    if 'a'<=c<='z':
        return ord(c) - ord('a') + 27
def nn(c):
    if 0<=c<=25:
        return chr(c + ord('A'))
    else:
        return chr(c - 27 + ord('a'))
def main():
    input=sys.stdin.readline
    N=int(input())
    gr=[[INF]*(53)for _ in range(53)]
    for _ in range(N):
	    P=input().rstrip()
	    gr[cc(P[0])][cc(P[5])]=1
    for i in range(53):gr[i][i]=0
    A=[]
    X=0
    floyd(gr)
    for i in range(53):
        for j in range(53):
            if gr[i][j]>0 and gr[i][j]!=INF:
                X+=1
                A.append(f'{nn(i)} => {nn(j)}')
    print(X)
    print(*A)
if __name__ == '__main__':
    main()
