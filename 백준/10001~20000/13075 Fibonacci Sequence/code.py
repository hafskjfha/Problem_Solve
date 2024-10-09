input=open(0).readline
mod=10**9
def mul(a,b):
    mat=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat[i][j]+=a[i][k] * b[k][j]
            mat[i][j]%=mod
    return mat
def fibo(N):
    rst=[[1,0],[0,1]]
    tmp=[[1,1],[1,0]]
    while N:
        if N&1:
            rst=mul(rst,tmp)
        tmp=mul(tmp,tmp)
        N>>=1
    print(rst[0][1])
def main():
    for _ in range(int(input())):
        fibo(int(input()))
main()
