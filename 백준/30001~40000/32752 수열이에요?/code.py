def main():
    n,l,r=map(int,input().split())
    a=[*map(int,input().split())]
    k=sorted(a)
    a[l-1:r]=sorted(a[l-1:r])
    if a==k:
        print(1)
        return
    print(0)
main()
