def main():
    from collections import defaultdict
    input=open(0).readline
    print=open(1,'w').write
    N,K,M=map(int,input().split())
    cp=defaultdict(dict)
    for _ in range(N):
        S=input().strip()
        for i in range(len(S)):
            if S[i]!=']':
                if S[i+1] in cp[S[i]]:
                    cp[S[i]][S[i+1]]+=1
                else:
                    cp[S[i]][S[i+1]]=1
    for i,k in cp.items():
        cp[i]=sorted(k.items(),key=lambda x:(-x[1],ord(x[0])))[0][0]
    ans='['
    c='['
    roop=["["]
    cr=set(['['])
    patten=""
    while 1:
        c=cp[c]
        if c in cr:
            patten="".join(roop[roop.index(c):])
            break
        roop.append(c)
        cr.add(c)
        ans+=c
        if c==']':
            break
    if K<=len(ans):
        for i in range(K-1,len(ans)):
            print(ans[i])
            M-=1
            if M==0:break
        if patten:
            print(patten*(M//len(patten)))
            M-=M//len(patten)*len(patten)
            print(patten[:M])
        elif M:print("."*M)
    else:
        K-=len(ans)
        if patten:
            print(patten[(K-1)%len(patten):])
            M-=len(patten[(K-1)%len(patten):])
            print(patten*(M//len(patten)))
            print(patten[:M-len(patten)*(M//len(patten))])
        else:
            print("."*M)
main()
