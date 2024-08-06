center={1,17,33,49,65}
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
    fl=set(list(fd.keys())[:16])
    print(kl)
    p=0
    for i in range(17):
        if kl[i] not in fl:
            p+=1
    return p

def AA(kd,fd,pc_r,fc_r):
    a=0
    for i in kd.keys():
        try:
            if kd[i]['rank']<pc_r and fd[i]['rank']>fc_r:
                a+=1
        except:
            a+=1
    return a


def sindelera(p_dict,f_dict,k):
    #pl=list(p_dict.keys())
    fl=list(f_dict.keys())
    sinde=[]
    for nname in fl:
        point=0
        f=f_dict[nname]
        r,g,t,c=f['rank'],f['group'],f['team'],f['class']
        try:
            p=p_dict[nname]
            pr,pg,pt,pc=p['rank'],g,t,p['class']
        except:
            pr,pg,pt,pc=81,g,t,6
        if pc>c:
            point+=10000*(pc-c)
        if r in center:
            point+=20000 if pc>c else 10000
        if pc!=1 and c==1:
            point+=30000*(k+AA(p_dict,f_dict,r,pr))
        sinde.append([point,-r,nname])
    sinde.sort(reverse=True)
    return sinde

 

def input_process(ppp,sset=set()):
    a=1
    i=0
    U={}
    name=[]
    #print(ppp)
    while i<len(ppp):
        
        if ppp[i]!='Group':
            name.append(ppp[i])
            i+=1
            continue
        r=grade(a)
        g=ppp[i+1]
        t=ppp[i+3]
        name=' '.join(name)
        sset.add(name)
        U[name]={'rank':a,'group':g,'team':t,'class':r}
        a+=1
        i+=4
        name=[]
    #print(U)
    return U,sset
    
def main():
    sss=input().split()
    m,p_set=input_process(sss,set())
    jjj=input().split()
    n,_=input_process(jjj)
    b=list(n.keys())
    if b[0] not in p_set:
        print(n[b[0]]['group'],n[b[0]]['team'],b[0].strip(),sep='\n')
        return
    p=LL(m,n)
    o=sindelera(m,n,p)
    po,_,name=o[0]
    print(n[name]['group'],n[name]['team'],name.strip(),sep='\n')
main()

    
    
    
    
    
    
    
