from collections import deque
input=open(0).readline
W=B=0
def bfs(board,v,x,y,t,K,N):
    global W,B
    q=deque([(x,y)])
    p=True
    co=[(x,y)]
    v[y][x]=K
    while q:
        x,y=q.popleft()
        for dx,dy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=dx<N and 0<=dy<N and v[dy][dx]<K:
                if board[dy][dx]==0:
                    p=False
                if board[dy][dx]==t:
                    q.append((dx,dy))
                    v[dy][dx]=K
                    co.append((dx,dy))
    if p:
        if board[co[0][1]][co[0][0]]==2:
            W+=len(co)
        else:
            B+=len(co)
        
        for x,y in co:
            board[y][x]=0
    return board,v

def sfs(V,S,board,N):
    global W,B
    q=deque([S])
    t=None
    c=1
    k=True
    V[S[1]][S[0]]=1
    while q:
        x,y=q.popleft()
        for dx,dy in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<N and 0<=dy<N and not V[dy][dx]:
                if t==None and board[dy][dx] in (1,2):
                    t= board[dy][dx]
                if board[dy][dx]==0:
                    c+=1
                    q.append((dx,dy))
                    V[dy][dx]=1
                if t!=None and board[dy][dx]in(1,2) and board[dy][dx]!=t:
                    k=False
    if k:
        if t==1:
            W+=c
        else:
            B+=c
    return V

def u(s):
    l=''
    j=False
    for p in s:
        if p=='(':
            j=True
        elif p==')':
            x,y=map(int,l.split(','))
            t=1 if s[0]=='B' else 2
            return t,x,y
        elif j:
            l+=p

def main():
    global W,B
    while 1:
        W=B=0
        K=1
        N,M=map(int,input().split())
        if N==0:break
        board=[[0]*N for _ in range(N)]
        v=[[0]*N for _ in range(N)]
        V=[[0]*N for _ in range(N)]
        w=N//2
        for z in range(M):
            a,x,y=u(input().strip())
            board[y+w][x+w]=a
            h=1 if a==2 else 2
            if z>2:
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    i,j=x+w+dx,y+w+dy
                    if 0<=i<N and 0<=j<N and board[j][i]==h:
                        board,v=bfs(board,v,i,j,board[j][i],K,N)
                        K+=1
        for i in range(N):
            for j in range(N):
                if board[j][i]==0 and not V[j][i]:
                    V=sfs(V,(i,j),board,N)
        print(W,B)
        
main()
