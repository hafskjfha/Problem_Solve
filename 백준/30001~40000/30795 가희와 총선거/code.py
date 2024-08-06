input=open(0).readline
center={1:1,2:17,3:33,4:49,5:65}
def grade(rank):
    if 0<rank<17:
        return 1
    elif 16<rank<33:
        return 2
    elif 32<rank<49:
        return 3
    elif 48<rank<65:
        return 4
    elif 64<rank<81:
        return 5
    else:
        return 6

def LL(kd,fd):
    kl=list(kd.keys())
    fl=set(fd.keys())
    p=0
    for i in range(0,17):
        if kl[i] not in fl:
            p+=1
    return p

def sindelera(p_dict,f_dict)

def input_process(ppp,sset=set()):
    a=1
    i=0
    U={}
    while i<len(ppp)-1:
   # print(i)
        name=''
        while 1:
            if ppp[i]=='Group':
                break
            name+=ppp[i]
            i+=1
        r=grade(a)
        i+=1
        g=ppp[i]
        i+=2
        t=ppp[i]
        i+=1
        sset.add(name)
        U[name]={'rank_p':a,'group':g,'team':t,'class':r}
        a+=1
    print(U)
    return U,sset
    
def main():
    sss=input().split()
    m,p_set=input_process(sss)
    jjj=input().split()
    n,_=input_process(jjj)
    b=list(n.keys())
    if b[0] not in p_set:
        print(n[b[0]]['group'],n[b[0]]['team'],b[0])
        return
    p=LL(m,n)
    print(n[b[0]]['group'],n[b[0]]['team'],b[0])
main()

    
    
    
    
    
    
    
    
