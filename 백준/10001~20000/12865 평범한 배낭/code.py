def main():
    import os
    input=os.read(0,os.stat(0).st_size).decode().split('\n').__iter__().__next__
    print=os.write
    exit=os._exit
    OK=os.EX_OK
    encode=str.encode
    N,K=map(int,input().split())
    dp=[[0]*(K+1) for _ in range(N+1)]
    P=[(0,0)]
    for _ in range(N):
        P.append(tuple(map(int,input().split())))
    for i in range(1,N+1):
        for j in range(1,K+1):
            if j<P[i][0]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-P[i][0]]+P[i][1])
    print(1,encode(f'{dp[N][K]}'))
    exit(OK)
main()
