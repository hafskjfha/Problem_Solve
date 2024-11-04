def k(N,B):
    if N==0:return '0'
    s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans=''
    while N:
        ans = s[N%B]+ans
        N//=B
    print(ans)
k(*map(int,input().split()))
