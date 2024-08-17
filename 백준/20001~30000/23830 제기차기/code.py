def sol(K,P,Q,R,S,A):
    tS=0
    for i in A:
        if i>K+R:
            tS+=i-P
        elif i<K:
            tS+=i+Q
        else:
            tS+=i
    return 0 if tS<S else 1

def main():
    INF=float('inf')
    N=int(input())
    A=[*map(int,input().split())]
    P,Q,R,S=map(int,input().split())
    start,end=1,100001
    ans=INF
    while start<=end:
        mid=(start+end)//2
        if sol(mid,P,Q,R,S,A):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    print(-1 if ans==INF else ans)
main()
