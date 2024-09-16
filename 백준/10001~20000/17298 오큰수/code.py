def main():
    N=int(input())
    A=[*map(int,input().split())]
    L=[-1]*N
    S=[0]
    for i in range(1,N):
        while S and A[S[-1]]<A[i]:
            L[S.pop()]=A[i]
        S.append(i)
    print(*L)
    return 1
main()
