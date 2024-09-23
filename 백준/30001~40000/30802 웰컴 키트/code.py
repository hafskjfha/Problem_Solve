from math import ceil
N=int(input())
w=[*map(int,input().split())]
T,P=map(int,input().split())
A=0
for i in w:
    A+=ceil(i/T)
print(A)
print(N//P,N%P)
