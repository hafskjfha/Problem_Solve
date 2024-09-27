from bisect import bisect_left
input=open(0).readline
N=int(input())
A=[tuple(map(int,input().split()))for _ in range(N)]
A.sort(key=lambda x:-x[0])    
B=[]
L=0
for j in A:
    i=j[1]
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        B[bisect_left(B,i)]=i
print(L)
