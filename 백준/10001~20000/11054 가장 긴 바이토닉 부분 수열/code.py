def LIS(A,N):
    import bisect
    B=[]
    L=0
    dp1=[1]*N
    dp2=[1]*N
    for j in range(N):
        i=A[j]
        if not B or B[-1]<i:
            B.append(i)
            L+=1
        else:
            k=bisect.bisect_left(B,i)
            B[k]=i
        dp1[j]=L
    L=0
    B=[]
    for j in range(N-1,-1,-1):
        i=A[j]
        if not B or B[-1]<i:
            B.append(i)
            L+=1
        else:
            k=bisect.bisect_left(B,i)
            B[k]=i
        dp2[j]=L
    return dp1,dp2
N=int(input())
a=[*map(int,input().split())]
dp1,dp2=LIS(a,N)
k=[]
for i in range(N):
    k.append(dp1[i]+dp2[i])
print(max(k)-1)
