input=open(0).readline
def sol(K,A,N,C):
    now=0
    t=0
    for i in range(N+1):
        if A[i]-now>K:
            t+=1
            if A[i]-now==K:now=A[i]
            else: now=A[i-1]
    return 0 if t>C else 1

def main():
    L,N,K=map(int,input().split())
    A=[*map(int,input().split())]+[L]
    start=A[0]
    for i in range(1,N+1):
        start=max(start,A[i]-A[i-1])
    end=ans=L
    while start<=end:
        mid=(start+end)//2
        if sol(mid,A,N,K):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    print(ans)
main()
