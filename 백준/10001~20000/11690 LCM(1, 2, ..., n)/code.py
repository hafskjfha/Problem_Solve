def main():
    N=int(input())
    prime=bytearray(N+1)
    mod=4294967296
    ans=1
    while ans*2<=N:ans*=2
    i=3
    for p in range(3,int(N**0.5)+1,2):
        if not prime[i]:
            c=i
            while c*i<=N:c*=i
            ans=ans*c%mod
            for j in range(i*i,N+1,i*2):
                prime[j]=1
        i+=2
    for i in range(i,N+1,2):
        if not prime[i]:
            ans=ans*i%mod
    print(ans)
                
main()
