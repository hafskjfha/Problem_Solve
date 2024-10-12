def main():
    input=open(0).readline
    print=open(1,'w').write
    S:list[str]=[]
    A=input().strip()
    B=list(input().strip())
    L=len(B)
    K=B[-1]
    append=S.append
    for i in A:
        append(i)
        if i==K and S[-L:]==B:
            del S[-L:] 
    print(''.join(S) or "FRULA")

main()
