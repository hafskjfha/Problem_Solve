input=open(0).readline
#TIOJZ: [0도,90도,180도,270도]spin
minos=[
    [(0,0),(-1,1),(0,1),(1,1)], #T1
    [(0,0),(0,1),(1,1),(0,2)], #T2
    [(0,0),(1,0),(2,0),(1,1)], #T3
    [(0,0),(-1,1),(0,1),(0,2)], #T4
    [(0,0),(0,1),(0,2),(0,3)], #I1
    [(0,0),(1,0),(2,0),(3,0)], #I2
    [(0,0),(1,0),(0,1),(1,1)], #O
    [(0,0),(0,1),(0,2),(-1,2)], #J1
    [(0,0),(0,1),(1,1),(2,1)], #J2
    [(0,0),(1,0),(0,1),(0,2)], #J3
    [(0,0),(1,0),(2,0),(2,1)], #J4
    [(0,0),(1,0),(1,1),(2,1)], #Z1
    [(0,0),(0,1),(-1,1),(-1,2)] #Z2
]
def try_place(board,N):
    ans=float('-inf')
    for i in range(N):
        for j in range(N):
            for k in minos:
                ts=0
                for dx,dy in k:
                    if 0<=i+dx<N and 0<=j+dy<N:
                        ts+=board[j+dy][i+dx]
                    else:
                        break
                else:
                    ans=max(ans,ts)
    return ans


def main() -> int:
    k=1
    while 1:
        N=int(input())
        if N==0:break
        board=[[*map(int,input().split())]for _ in range(N)]
        print(f'{k}. {try_place(board,N)}')
        k+=1
    return 1

main()
