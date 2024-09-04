import bisect

N=int(input())
A=[*map(int,input().split())]
B=[]
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        k=bisect.bisect_left(B,i)
        B[k]=i
print(L)
