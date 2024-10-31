def main():
    import os
    input=os.read(0,os.stat(0).st_size).decode().split('\n').__iter__().__next__
    print=os.write
    exit=os._exit
    OK=os.EX_OK
    encode=str.encode
    N,G,K=map(int,input().split())
    O0=[]
    O1=[]
    for _ in range(N):
        S,L,O=map(int,input().split())
        O1.append((S,L)) if O else O0.append((S,L))     
    left,right=0,2*10**9
    ans=0
    while left<=right:
        mid=(left+right)//2
        A=0
        for s,l in O0:
            A+=s*max(1,mid-l)
        P=[]
        for s,l in O1:
            y=s*max(1,mid-l)
            P.append(y)
            A+=y
        P.sort()
        for _ in range(K):
            if P:
                A-=P.pop()
            else:
                break
        if A>G:
            right=mid-1
        else:
            ans=mid
            left=mid+1
    print(1,encode(f"{ans}"))
    exit(OK)


main()
