from bisect import bisect_left
f=bisect_left
N=int(input())
A=[*map(int,input().split())]
B=[]
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        B[f(B,i)]=i
print(L)
