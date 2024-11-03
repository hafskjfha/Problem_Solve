def main():
    input=open(0).readline
    print=open(1,'w').write
    N=int(input())
    A=[*map(int,input().split())]
    M=int(input())
    if N==0:
        print(f'{A[0]%M}')
    elif N==1:
        print(f'{pow(A[1],A[0],M)}')
    else:
        ans=pow(A[1],A[0],M-1)
        ans+=M-1
        print(f'{pow(A[2],ans,M)}')
main()      
