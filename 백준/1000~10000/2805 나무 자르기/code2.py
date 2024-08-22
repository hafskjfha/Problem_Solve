from collections import Counter
input=open(0).readline
def sol(K,A,M):
    s=0
    for i,j in A.items():
        if i<=K:continue
        s+=(i-K)*j
        if s>=M:return 1
    return 0 if s<M else 1

def main():
    N,M=map(int,input().split())
    A=Counter(map(int,input().split()))
    start,end=0,1000000000
    while start<=end:
        mid=(start+end)//2
        if sol(mid,A,M):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    print(ans)
main()
