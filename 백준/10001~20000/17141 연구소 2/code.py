from itertools import combinations
from collections import deque
input=open(0).readline
def bfs(S,k,N,board,V):
    q=deque()
    r=0
    mT=0
    for sx,sy in S:
        V[sy][sx]=k
        q.append((sx,sy,0))
        r+=1
    while q:
        x,y,t=q.popleft()
        mT=max(mT,t)
        for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=dx<N and 0<=dy<N and V[dy][dx]<k and board[dy][dx]!="1":
                q.append((dx,dy,t+1))
                r+=1
                V[dy][dx]=k
    return r,mT,V
def main():
    N,M=map(int,input().split())
    board=[]
    vir=[]
    p=0
    ans=2501
    V=[[0]*N for _ in range(N)]
    k=1
    for i in range(N):
        temp=input().split()
        for j in range(N):
            if temp[j]=="2":
                vir.append((j,i))
                p+=1
            elif temp[j]=="0":
                p+=1
        board.append(temp)
    combs=combinations(vir,M)
    for u in combs:
        r,mt,V=bfs(u,k,N,board,V)
        if r==p:
            ans=min(mt,ans)
        k+=1
    print(ans if ans!=2501 else -1)

main()
