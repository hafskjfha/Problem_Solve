A,B=map(int,input().split())
D=10**9+7
print((pow(A,B,D)-1)*pow(A-1,D-2,D)%D if A>1 else B%D)
