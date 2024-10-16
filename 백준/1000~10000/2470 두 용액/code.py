input=open(0).readline
def main():
    N=int(input())
    A=sorted(map(int,input().split()))
    i,j=0,N-1
    ansi,ansj=0,N-1
    mina=float('inf')
    while i<j:
        if A[i]+A[j]<0:
            if abs(0-abs(A[i]+A[j]))<abs(0-abs(mina)):
                mini,minj=i,j
                mina=A[i]+A[j]
            i+=1
    
        elif A[i]+A[j]>0:
            if abs(0-abs(A[i]+A[j]))<abs(0-abs(mina)):
                mini,minj=i,j
                mina=A[i]+A[j]
            j-=1
        else:
            mini,minj=i,j
            mina=A[i]+A[j]
            break
    print(A[mini],A[minj])
main()
