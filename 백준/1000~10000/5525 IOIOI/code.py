def getpi(p):
    m=len(p)
    PI=[0]*m
    j=0
    for i in range(1,m):
        while j and p[i]!=p[j]:
            j=PI[j-1]
        if p[i]==p[j]:
            j+=1
            PI[i]=j
    return PI
 
def kmp(s,p):
    PI=getpi(p)
    ans=[]
    n,m,j=len(s),len(p),0
    for i in range(n):
        while j and s[i]!=p[j]:
            j=PI[j-1]
        if s[i]==p[j]:
            if j==m-1:
                ans.append(i-m+1)
                j=PI[j]
            else:
                j+=1
    return len(ans)

def main():
    N=int(input())
    M=int(input())
    S=input()
    pa='IOI'
    pa+='OI'*(N-1)
    print(kmp(S,pa))

main()
