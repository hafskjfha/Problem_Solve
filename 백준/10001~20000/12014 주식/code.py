from bisect import bisect_left
def main():
    for t in range(1,int(input())+1):
        N,K=map(int,input().split())
        A=[*map(int,input().split())]
        B=[]
        L=0
        for i in A:
            if not B or B[-1]<i:
                B.append(i)
                L+=1
            else:
                B[bisect_left(B,i)]=i
        print(f'Case #{t}')
        print(0)if K>L else print(1) 
main()
