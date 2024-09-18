import bisect,sys
input=sys.stdin.readline

N=int(input())
A=[[*map(int,input().split())] for _ in range(N)]
A.sort(key=lambda x:x[0])
B=[]
A=[i[1]for i in A]
L=0
for i in A:
    if not B or B[-1]<i:
        B.append(i)
        L+=1
    else:
        k=bisect.bisect_left(B,i)
        B[k]=i
print(N-L)
