from collections import deque
input=open(0).readline 
def bfs(V,board,sx,sy,k):
    q=deque([(sx,sy)])
    c=1
    p=[(sx,sy)]
    V[sy][sx]=k
    while q:
        x,y=q.popleft()
        for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=dx<6 and 0<=dy<12 and V[dy][dx]<k and board[dy][dx]==board[y][x]:
                q.append((dx,dy))
                c+=1
                p.append((dx,dy))
                V[dy][dx]=k
    
    if c>3:
        t=True
        for x,y in p:
            board[y][x]='.'
    else:
        t=False
    return V,board,t

def drop(board):
    for i in range(6):
        oy=-1
        jq=[]
        for j in range(11,-1,-1):
            if board[j][i]=="." and oy==-1:
                oy=j
            elif board[j][i]!="." and oy!=-1:
                jq.append(board[j][i])
                board[j][i]="."
        for k in jq:
            board[oy][i]=k
            oy-=1
    
    return board

def main():
    board=[list(input().strip())for _ in range(12)]
    V=[[0]*6 for _ in range(12)]
    k=1
    combo=0
    while 1:
        C=True
        for i in range(6):
            for j in range(12):
                if V[j][i]<k and board[j][i]!=".":
                    V,board,p=bfs(V,board,i,j,k)
                    if p:C=False
        if C:
            print(combo)
            break
            return 1
        
        board=drop(board)
        k+=1
        combo+=1
main()
