input=open(0).readline
def two_pointer(N,A,i):
    S=A[i]
    j,k=i+1,N-1
    mina=float('inf')
    minj,mink =j,k
    while j<k:
        current_sum=S+A[j]+A[k]
        if abs(current_sum)<abs(mina):
            minj,mink=j,k
            mina=current_sum
        if current_sum<0:
            j+=1
        elif current_sum>0:
            k-=1
        else:
            return 0,i,j,k  

    return mina,i,minj,mink

def main():
    N=int(input())
    A=sorted(map(int,input().split()))
    mina=float('inf')

    for i in range(N-2):
        S,i,j,k=two_pointer(N,A,i)
        if S==0: 
            mini,minj,mink=i,j,k
            break
        if abs(S)<abs(mina):
            mini,minj,mink=i,j,k
            mina=S

    print(A[mini],A[minj],A[mink])

main()
