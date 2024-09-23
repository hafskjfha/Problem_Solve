from bisect import bisect_left 
input=open(0).readline
def main():
    for T in range(1,int(input())+1):
        N=int(input())
        A=[int(input())for _ in range(N)]
        c=0
        for i in range(N):
            B=[]
            L=0
            for j in range(i,N):
                v=A[j]
                if not B or B[-1]<v:
                    B.append(v)
                    L+=1
                else:
                    B[bisect_left(B,v)]=v
                c+=L
        print(f"Case #{T}: {c}")

main()
