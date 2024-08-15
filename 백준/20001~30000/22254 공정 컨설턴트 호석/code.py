import heapq
push=heapq.heappush
pop=heapq.heappop
def sol(A,B,X):
    pq=[0]*B
    for i in A:
        t=pop(pq)+i
        if t>X:return 0
        push(pq,t)
    return 1
        
def main():
    N,X=map(int,input().split())
    a=N
    K=[*map(int,input().split())]
    S,E=1,N
    while S<=E:
        M=(S+E)//2
        if sol(K,M,X):
            a=M
            E=M-1
        else:
            S=M+1
    print(a)
main()
