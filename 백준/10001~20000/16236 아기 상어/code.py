from collections import deque
input=open(0).readline
def bfs(board,N,V,k,sx,sy,S):
    q=deque([(sx,sy,0)])
    pl=[]
    while q:
        x,y,t=q.popleft()
        if pl and pl[0][0]<t:continue
        if 0<board[y][x]<S:pl.append((t,y,x))
        for dx,dy in ((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
            if 0<=dx<N and 0<=dy<N and board[dy][dx]<=S and V[dy][dx]<k :
                q.append((dx,dy,t+1))
                V[dy][dx]=k
    pl.sort()
    return (*pl[0],V,board) if pl else (0,sy,sx,V,board)
    
def main() ->int:
    N=int(input())
    board=[]
    V=[[0]*N for _ in range(N)]
    for i in range(N):
        temp=[*map(int,input().split())]
        for j in range(N):
            if temp[j]==9:
                nx,ny=j,i
        board.append(temp)
    
    k=1
    T=0
    Lv=2
    exp=0
    while 1:
        board[ny][nx]=0
        t,ny,nx,V,board=bfs(board,N,V,k,nx,ny,Lv)
        if t==0:
            print(T)
            return 1
        board[ny][nx]=9
        exp+=1
        if exp==Lv:
            Lv+=1
            exp=0
        T+=t
        k+=1

main()
