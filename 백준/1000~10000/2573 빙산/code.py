from collections import deque
input=open(0).readline
def bfs(V,A,N,M,k,sx,sy):
    c=1
    q=deque([(sx,sy)])
    V[sy][sx]=k
    while q:
        x,y=q.popleft()
        for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
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
    ices=set()
    ttemp=[[],[]] #녹일수 있는 바다 담는 리스트
    for i in range(N):
        temp=[*map(int,input().split())]
        for j in range(M):
            if temp[j]:
                ice+=1
                ices.add((j,i))
            else:
                ttemp[1].append((j,i))
        A.append(temp)
    k=1
    while 1:
        u=k%2
        D=False #얼음이 녹았는지 체크 하는 변수
        for x,y in ttemp[u]:
            P=False
            for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=dx<M and 0<=dy<N and A[dy][dx]:
                    P=True #네 방향중 하나라도 얼음이 접해있는 바다
                    if A[dy][dx]:
                        A[dy][dx]-=1
                        if A[dy][dx]==0:
                            ttemp[0 if u else 1].append((dx,dy))
                            ices.remove((dx,dy))
                            D=True #녹일수 있으면 true
                            ice-=1
                            if ice==0: #다 녹으면 처리
                                print(0)
                                return 1
            if P:
                ttemp[0 if u else 1].append((x,y))
        ttemp[u]=[]#바다 리스트 갱신
        if D: #얼음이 1개 이상녹았나?
            for i,j in ices:
                V,icek=bfs(V,A,N,M,k,i,j)
                if icek!=ice: #얼음덩어리 나누어짐
                    print(k)
                    return 1
                break
        k+=1
            
main()

