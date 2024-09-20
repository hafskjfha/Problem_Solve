from heapq import heappush,heappop
input=open(0).readline
def main():
    for _ in range(1,int(input())+1):
        N=int(input())
        A=[*map(int,input().split())]
        pq=[]
        for i in A:heappush(pq,i)
        ans=0
        while len(pq)>1:
            k=heappop(pq)+heappop(pq)
            ans+=k
            heappush(pq,k)
        print(ans)
main()
