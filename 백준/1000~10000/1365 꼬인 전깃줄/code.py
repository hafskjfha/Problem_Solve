from bisect import bisect_left
N=int(input())
B=[]
L=0
for i in map(int,input().split()):
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        B[bisect_left(B,i)]=i
print(N-L)
