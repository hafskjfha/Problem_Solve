from bisect import bisect_left
input=open(0).readline
def main():
    while 1:
        N=input()
        if N=='':break
        A=[*map(int,input().split())]
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
