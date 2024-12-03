def main():
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    ans=0
    l,r=0,10**9
    while l<=r:
        mid=(l+r)//2
        t,c,f=0,1,True
        for i in a:
            if i>mid:
                f=False
                break
            if t+i>mid:
                c+=1
                if c>m:
                    f=False
                    break
                t=i
            else:
                t+=i
        if c>m:f=False
        #print(l,mid,r,c,f)
        if f:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)


main()
