input=open(0).readline
print=open(1,'w').write
def main():
    from collections import defaultdict
    A=defaultdict(int)
    L=[]
    S=0
    for _ in range(int(input())):
        W=input().strip()
        B=10**(len(W)-1)
        for i in W:
            A[i]+=B
            B//=10
        L.append(W)
    k=9
    C=[]
    for a,_ in sorted(A.items(),key=lambda x:-x[1]):
        C.append((a,k))
        k-=1
    for w in L:
        for a,k in C:
            w=w.replace(a,str(k))
        S+=int(w)
    print(str(S))

main()
