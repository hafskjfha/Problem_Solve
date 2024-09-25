from collections import defaultdict
input=open(0).readline
def base36(N):
    if N==0:return "0"
    r=""
    a="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while N:
        r=a[N%36]+r
        N//=36
    return r
def main():
    N=int(input())
    A=[input().strip() for _ in range(N)]
    K=int(input())
    D=defaultdict(int)
    for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        x,y=0,0
        for h in A:
            x+=int(h,36)
            y+=int(h.replace(i,"Z"),36)
        D[i]=y-x
    D=sorted(D.items(),key=lambda x:(-x[1],x[0]))
    ans=0
    for h in A:
        for i in range(K):
            if D[i][1]==0:break
            h=h.replace(D[i][0],"Z")
        ans+=int(h,36)
    print(base36(ans))
main()
