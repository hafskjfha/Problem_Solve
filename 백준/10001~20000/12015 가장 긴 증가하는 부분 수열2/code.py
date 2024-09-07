from bisect import bisect_left 
f=bisect_left
input()
A=[*map(int,input().split())]
B=[]
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        k=f(B,i)
        B[k]=i
print(L)
