input=open(0).readline
def sol(K,A,C):
    now=0
    c=0
    for i in A:
        if i-now>=K:
            c+=1
            now=i
    return 1 if c>C else 0
def main():
    N,M,L=map(int,input().split())
    A=[int(input())for _ in range(M)]+[L]
    for _ in range(N):
        C=int(input())
        start,end=0,L
        ans=0
        while start<=end:
            mid=(start+end)//2
            if sol(mid,A,C):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        print(ans)
main()
