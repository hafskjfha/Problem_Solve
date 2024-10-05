from bisect import bisect_left

N=int(input())
A=[*map(int,input().split())]
h={A[i]:i for i in range(N)}
B=[*map(int,input().split())]
C=[]
L=0
for i in [h[B[i]]for i in range(N)]:
    if not C or C[-1]<i:
        C.append(i)
        L+=1
    else:
        C[bisect_left(C,i)]=i
print(L)
