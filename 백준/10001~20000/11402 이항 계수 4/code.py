def l(n,m,p):
    from math import comb
    r=1
    while n or m:
        ni=n%p
        mi=m%p
        r=r*comb(ni,mi)%p
        n//=p
        m//=p
    return r
print(l(*map(int,input().split())))
