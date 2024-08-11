input=open(0).readline
sp={}
db={}
def main():
    b=0
    st={input().strip():int("0",2) for _ in range(int(input()))}
    for _ in range(int(input())):
        c,*p=input().strip().split()
        if c=="U":
            sn=p[0]
            if db.get(st[sn],0):
                db[st[sn]]-=1
            sf=p[1].split(",")
            kb=["0"]*10
            for k in sf:
                try:
                    kb[sp[k]]="1"
                except:
                    sp[k]=b
                    b+=1
                    kb[sp[k]]="1"
            p=int("".join(kb),2)
            st[sn]=p
            try:
                db[p]+=1
            except:
                db[p]=1
        elif c=="G":
            jb=["0"]*10
            for j in p[0].split(","):
                try:
                    jb[sp[j]]="1"
                except:
                    print(0)
                    break
            else:
                p=int("".join(jb),2)
                ans=0
                for i in db.keys():
                    if i&p==p:
                        ans+=db[i]
                print(ans)                    
main()
