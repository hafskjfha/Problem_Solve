def main():
    input=open(0).readline
    print=open(1,'w').write
    from heapq import heappush,heappop,heapify
    for _ in range(int(input())):
        input()
        pq=[*map(int,input().split())]
        heapify(pq)
        ans=0
        while len(pq)>1:
            a,b=heappop(pq),heappop(pq)
            ans+=a+b
            heappush(pq,a+b)
        print(f'{ans}\n')

main()
