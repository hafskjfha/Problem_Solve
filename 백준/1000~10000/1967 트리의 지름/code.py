import sys
sys.setrecursionlimit(10**5)
input=open(0).readline
def dfs(gr,di,x,w):
    for a,b in gr[x]:
        if di[a]==-1:
            di[a]=w+b
            dfs(gr,di,a,w+b)
    return di

def main():
    N=int(input())
    gr=[[]for _ in range(N+1)]
    for _ in range(N-1):
        a,b,c=map(int,input().split())
        gr[a].append((b,c))
        gr[b].append((a,c))
    d1=[-1]*(N+1)
    d2=[-1]*(N+1)
    d1[1]=0
    d1=dfs(gr,d1,1,0)
    j=k=0
    for i in range(1,N+1):
        if d1[i]>j:
            k=i
            j=d1[i]
    d2[k]=0
    print(max(dfs(gr,d2,k,0)))

main()
