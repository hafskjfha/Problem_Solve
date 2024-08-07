from collections import deque
dxl=[1,-1,0,0]
dyl=[0,0,1,-1]
U={'E':0,'W':1,'S':2,'N':3}
def attack(B,G,x,y,k,N,M):
    t=1
    dx,dy=dxl[k],dyl[k]
    G[y][x]='F'
    q=deque([[x,y]])
    while q:
        x,y=q.popleft()
        for i in range(1,B[y][x]):
            jx,jy=x+dx*i,y+dy*i
            if 0<=jx<M and 0<=jy<N and G[jy][jx]!='F':
                t+=1
                q.append([jx,jy])
                G[jy][jx]='F'
    return G,t
def main():
    input=open(0).readline
    p=0
    N,M,R=map(int,input().split())
    B=[[*map(int,input().split())]for _ in range(N)]
    G=[['S']*M for _ in range(N)]
    for _ in range(R):
        X,Y,D=input().strip().split()
        X,Y=int(Y)-1,int(X)-1
        if G[Y][X]!='F':
            G,ppoint=attack(B,G,X,Y,U[D],N,M)
            p+=ppoint
        X,Y=map(int,input().split())
        G[X-1][Y-1]='S'
    print(p)
    for i in G:print(*i)
main()
