input=open(0).readline
def main():
    N=int(input())
    D={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
    F=set()
    S:list[str]=[]
    for _ in range(N):
        M=input().strip()
        S.append(M)
        P=10**(len(M)-1)
        for i in M:
            if P==10**(len(M)-1):F.add(i)
            D[i]+=P
            P//=10
    u=[float('inf'),None]
    for i in 'ABCDEFGHIJ':
        if i not in F and D[i]<u[0]:
            u[0],u[1]=D[i],i
    K={}
    if u[1]!=None:
        del D[u[1]]
    D=sorted(D.items(),key=lambda x:-x[1])
    X=9
    for a,i in D:
        if i!=0:
            K[a]=X
            X-=1
        else:
            break
    if u[1]!=None:
        K[u[1]]=X
    for a,p in K.items():
        for i in range(N):
            S[i]=S[i].replace(a,str(p))
    ans=0
    for m in S:ans+=int(m)
    print(ans)
main()
