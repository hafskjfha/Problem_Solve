def sol(A,N,K,M):
    c=0
    for i in range(1,N+2):
        if A[i]-A[i-1]>K:
            c+=(A[i]-A[i-1]-1)//K
    return 0 if c>M else 1
def main():
    N,M,L=map(int,input().split())
    A=[0]+[*map(int,input().split())]+[L]
    A.sort()
    start,end=1,1001
    ans=0
    while start<=end:
        mid=(start+end)//2
        if sol(A,N,mid,M):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    print(ans)
main()
