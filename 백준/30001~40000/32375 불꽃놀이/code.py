def main():
    n,k=map(int,input().split())
    a=sorted(map(int,input().split()))

    p=-1
    for i in range(n):
        if a[i]>=k:
            break
        p=i

    s,b,c=[],[],0
    if p!=-1:
        s=a[:i+1]
        b=a[i+1:]
        i,j=0,len(s)-1
        while i<j:
            if s[i]+s[j]<k:
                i+=1
            else:
                c+=1
                i+=1
                j-=1 
    else:
        b=a

    print(len(b)+c or -1)
main()