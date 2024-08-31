from collections import deque
from copy import deepcopy
input=open(0).readline
def bfs(V,A,N,M,k,sx,sy):
    c=1
    q=deque([(sx,sy)])
    V[sy][sx]=k
    while q:
        x,y=q.popleft()
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<M and 0<=dy<N and V[dy][dx]<k and A[dy][dx]:
                q.append((dx,dy))
                V[dy][dx]=k
                c+=1
    return V,c

def main():
    N,M=map(int,input().split())
    V=[[0]*M for _ in range(N)]
    sea=[]
    A=[]
    ice=0
    for i in range(N):
        temp=[*map(int,input().split())]
        for j in range(M):
            if temp[j]:
                ice+=1
            else:
                sea.append((j,i))
        A.append(temp)
    k=1
    while 1:
        ttemp=[]
        D=False
        for x,y in sea:
            P=False
            for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=dx<M and 0<=dy<N and A[dy][dx]:
                    P=True
                    if A[dy][dx]:
                        A[dy][dx]-=1
                        if A[dy][dx]==0:
                            ttemp.append((dx,dy))
                            D=True
                            ice-=1
                            if ice==0:
                                print(0)
                                return 1
            if P:
                ttemp.append((x,y))
        sea=deepcopy(ttemp)
        if D:
            for i in range(N):
                for j in range(M):
                    if A[i][j]:
                        V,icek=bfs(V,A,N,M,k,j,i)
                        if icek!=ice:
                            print(k)
                            return 1
                        else:break
                else:
                    continue
                break
                
        k+=1            
main()
