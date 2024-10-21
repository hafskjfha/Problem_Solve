def main():
    input=open(0).readline
    N,M=map(int,input().split())
    Sx,Sy=-1,-1
    B=[]
    for i in range(N):
        t=list(input().strip())
        for j in range(M):
            if Sx!=-1:break
            if t[j]=='I':
                Sx,Sy=j,i
        B.append(t)
    from collections import deque
    V=[[False]*M for _ in range(N)]
    ans=0
    q=deque([(Sx,Sy)])
    while q:
        x,y=q.popleft()
        for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=dx<M and 0<=dy<N and V[dy][dx]==False and B[dy][dx]!='X':
                V[dy][dx]=True
                q.append((dx,dy))
                if B[dy][dx]=='P':
                    ans+=1
    print(ans or 'TT')
        
    
    

main()
