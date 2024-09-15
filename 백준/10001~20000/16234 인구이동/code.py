from collections import deque
input=open(0).readline
def bfs(ddang:list[list[int]],V:list[list[int]],k:int,sx:int,sy:int,N:int,L:int,R:int)->tuple[list[list[int]],list[list[int]],int]:
    q=deque([(sx,sy)])
    V[sy][sx]=k
    h=[(sx,sy)]
    p=ddang[sy][sx]
    w:int=1
    while q:
        x,y=q.popleft()
        for dx,dy in ((x+1,y),(x-1,y),(x,y-1),(x,y+1)):
            if 0<=dx<N and 0<=dy<N and V[dy][dx]<k and L<=abs(ddang[y][x]-ddang[dy][dx])<=R:
                q.append((dx,dy))
                V[dy][dx]=k
                h.append((dx,dy))
                p+=ddang[dy][dx]
                w+=1
    if w==1:
        return ddang,V,0
    p=p//w
    for x,y in h:
        ddang[y][x]=p
    return ddang,V,1
def main():
    N,L,R=map(int,input().split())
    k:int=1
    ddang=[[*map(int,input().split())]for _ in range(N)]
    V=[[0]*N for _ in range(N)]
    while 1:
        C:bool=False
        for i in range(N):
            for j in range(N):
                if V[j][i]<k:
                    ddang,V,c=bfs(ddang,V,k,i,j,N,L,R)
                    if c:C=True
        if not C:
            print(k-1)
            return 1
        k+=1

main()
