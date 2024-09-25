from bisect import bisect_left
input=open(0).readline
def main():
    for _ in range(int(input())):
        N=int(input())
        A=[int(input())for _ in range(N)]
        B=[]
        L=0
        for i in A:
            if not B or B[-1]<i:
                B.append(i)
                L+=1
            else:
                B[bisect_left(B,i)]=i
        print(L)
main()
