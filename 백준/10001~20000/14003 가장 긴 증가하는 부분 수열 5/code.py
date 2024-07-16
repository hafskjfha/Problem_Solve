import bisect

N=int(input())
A=[*map(int,input().split())]
B=[]
R=[]
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        R.append(L)
        L+=1
    else:
        k=bisect.bisect_left(B,i)
        R.append(k)
        B[k]=i
print(L)
S=[]
z=L
while R:
    v=R.pop()
    if v==L-1:
        S.append(A.pop())
        L-=1
    else:
        A.pop()
    if L==-1:
        break
for i in range(z):
    print(S.pop(),end=' ')
