from bisect import bisect_left
input=open(0).readline

N=int(input())

A=[[*map(int,input().split())] for _ in range(N)]
A.sort(key=lambda x:x[0])
B=[]
ip={i[1]: i[0] for i in A}
R=[]
A=list(ip.keys())
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        R.append(L)
        L+=1
    else:
        k=bisect_left(B,i)
        R.append(k)
        B[k]=i
print(N-L)
S=set()
z=L
while R:
    v=R.pop()
    if v==L-1:
        S.add(A.pop())
        L-=1
    else:
        A.pop()
    if L==-1:
        break
P=[]
for i in ip.keys():
    if i not in S:
        P.append(ip[i])
print(*sorted(P),sep='\n')
