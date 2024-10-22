def main():
    from collections import deque     
    input=open(0).readline
    print=open(1,'w').write
    N=int(input())
    B=[list(input().strip())for _ in range(N)]
    def bfs(Sx,Sy,B):
        q=deque([(Sx,Sy)])
        c=1
        B[Sy][Sx]=2
        while q:
            x,y=q.popleft()
            for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=dx<N and 0<=dy<N and B[dy][dx]=='1':
                    c+=1
                    B[dy][dx]=2
                    q.append((dx,dy))
        return c
    A=[]
    for x in range(N):
        for y in range(N):
            if B[y][x]=='1':
                A.append(bfs(x,y,B))
    
    print(f'{len(A)}\n'+'\n'.join(map(str,sorted(A))))
main()
