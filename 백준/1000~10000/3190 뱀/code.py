from collections import deque
input=open(0).readline
def main():
    N=int(input())
    board=[[0]*N for _ in range(N)]
    board[0][0]=1
    for _ in range(int(input())):
        y,x=map(int,input().split())
        board[y-1][x-1]=2
    L=deque()
    for _ in range(int(input())):
        X,C=input().split()
        L.append((int(X),C))
    J=deque([(0,0)])
    startx,starty=0,0
    endx,endy=0,0
    S=0
    W=0
    U=[(1,0),(0,1),(-1,0),(0,-1)]
    mt,c=L.popleft()
    T=1
    while 1:
        startx+=U[W][0]
        starty+=U[W][1]
        if 0<=startx<N and 0<=starty<N and board[starty][startx] in (0,2):
            if board[starty][startx]==2:
                board[starty][startx]=1
                J.append((startx,starty))
            else:
                board[starty][startx]=1
                board[endy][endx]=0
                J.append((startx,starty))
                J.popleft()
                endx,endy=J[0]
        else:
            print(T)
            return 1
        if T==mt:
            if c=="L":
                W-=1
                if W<0:W=3
            else:
                W+=1
                if W>3:W=0
            if L:
                mt,c=L.popleft()
        T+=1
        
main()
