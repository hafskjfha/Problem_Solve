from math import ceil
input=open(0).readline
def main():
    N,T=map(int,input().split())
    tier={}
    rank=1
    for _ in range(T):
        name,K=input().split()
        if K[-1]=='%':
            K=int(K.replace('%',''))
            MK=N*K//100
            tier[name]=[MK,[rank,rank+MK-1]]
            rank+=MK
            N-=MK
        else:
            K=min(N,int(K))
            tier[name]=[K,[rank,rank+K-1]]
            rank+=K
            N-=K
    if N:
        print('Invalid System')
        return 1
    Frend=input().strip()
    if Frend[-1] in ('1','2','3','4'):
        fkp=int(Frend[-1])
        ft1=Frend[:-1]
        j=tier.get(ft1,0)
        if j:
            print(u)
            KF=j[0]
            p=ceil(KF/4)
            fk1=min(p,KF)
            KF-=fk1
            fk2=min(p,KF)
            KF-=fk2
            fk3=min(p,KF)
            KF-=fk3
            fk4=min(p,KF)
            u=[0,fk1,fk2,fk3,fk4]
            if u[fkp]:
                aa=sum(u[:fkp])
                print(aa+j[1][0],j[1][1]-sum(u[fkp+1:]))
                
            else:
                print('Liar')
        else:
            print('Liar')
            return 1
    else:
        if (p:=tier.get(Frend,0)):
            print(*p[1])
            return 1
        else:
            print('Liar')
            return 1
            
main()
