def main():
    import os
    input=os.read(0,1<<19).decode().split('\n').__iter__().__next__
    print=os.write
    exit=os._exit
    OK=os.EX_OK
    encode=str.encode
    N=int(input())
    A=[*map(int,input().split())]
    i,j=0,N-1
    ans=min(A[i],A[j])*(j-i-1)
    while i+1<j:
        ans=max(ans,min(A[i],A[j])*(j-i-1))
        if A[i]<A[j]:
            i+=1
        else:
            j-=1
    print(1,encode(f'{ans}'))
    exit(OK)
main()
