def main():
    input=open(0).readline
    print=open(1,'w').write
    from math import ceil
    N=int(input())
    A=[*map(int,input().split())]
    B,C=map(int,input().split())
    ans=N
    for i in A:
        k=i-B
        if k>0:
            ans+=ceil(k/C)
    print(str(ans))
main()
