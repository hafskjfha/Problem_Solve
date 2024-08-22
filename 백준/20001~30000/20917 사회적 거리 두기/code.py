input=open(0).readline
def sol(K,A,N,S):
    now=A[0]
    c=1
    for i in range(1,N):
        if A[i]>=now+K:
            c+=1
            now=A[i]
    return 0 if c<S else 1

def main():
    for _ in range(int(input())):
        N,S=map(int,input().split())
        A=[*map(int,input().split())]
        A.sort()
        start,end=1,A[-1]-A[0]
        while start<=end:
            mid=(start+end)//2
            if sol(mid,A,N,S):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        print(ans)
main()
