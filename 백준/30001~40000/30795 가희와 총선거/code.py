center={1,17,33,49,65}
def grade(rank):
    return (rank-1) // 16 + 1

def LL(kd,fd):
    p=0
    for n,i in kd.items():
        if i['class']==1 and fd.get(n,{}).get('class',6)!=1:
            p+=1
    return p


def sindelera(p_dict,f_dict,k):
    sinde=[]
    for n in f_dict.keys():
        point=0
        na=n.split(';')
        nname=na[2]
        g,t=na[0],na[1]
        f=f_dict[n]
        r,c=f['rank'],f['class']
        try:
            p=p_dict[f'{g};{t};{nname}']
            pc=p['class']
        except:
            pc=6
        if pc>c:
            point+=10000*(pc-c)
        if r in center:
            point+=20000 if pc>c else 10000
        if pc!=1 and c==1:
            point+=30000*(k)
        sinde.append([point,-r,n])
    sinde.sort(reverse=True)
    return sinde

 

def input_process(ppp):
    a=1
    i=0
    U={}
    name=[]
    while i<len(ppp):
        if ppp[i]!='Group':
            name.append(ppp[i])
            i+=1
            continue
        r=grade(a)
        g=ppp[i+1]
        t=ppp[i+3]
        name=' '.join(name)
        U[f'{g};{t};{name}']={'rank':a,'class':r}
        a+=1
        i+=4
        name=[]
    return U
    
def main():
    sss=input().split()
    m=input_process(sss)
    jjj=input().split()
    n=input_process(jjj)
    p=LL(m,n)
    o=sindelera(m,n,p)
    po,_,name=o[0]
    print(name.replace(';','\n'))
main()

