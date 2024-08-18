input=open(0).readline
def sol(K,A,N,C):
    now=A[0]
    c=1
    for i in range(1,N):
        if A[i]>=now+K:
            c+=1
            now=A[i]
    return 0 if c<C else 1
def main():
    N,C=map(int,input().split())
    A=[int(input())for _ in range(N)]
    A.sort()
    start,end=1,A[-1]-A[0]
    while start<=end:
        mid=(start+end)//2
        if sol(mid,A,N,C):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    print(ans)
main()
