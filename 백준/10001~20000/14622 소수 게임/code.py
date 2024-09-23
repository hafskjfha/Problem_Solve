from heapq import heappush,heappop
push=heappush
pop=heappop
def eratos():
    is_prime = [1] * (5000001)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, 2237):
        if is_prime[i]:
            for j in range(i*2,5000001,i):
                is_prime[j] = 0

    return is_prime
def main():
    prime=eratos()
    dea=guu=0
    says=set()
    dpq=[]
    gpq=[]
    N=int(input())
    for _ in range(N):
        a,b=map(int,input().split())
        if prime[a]:
            if a in says:
                dea-=1000
            else:
                says.add(a)
                push(gpq,-a)
        else:
            if dpq.__len__()<3:
                guu+=1000
            else:
                c,d,f=pop(dpq),pop(dpq),pop(dpq)
                guu+=-f
                push(dpq,c)
                push(dpq,d)
                push(dpq,f)

        if prime[b]:
            if b in says:
                guu-=1000
            else:
                says.add(b)
                push(dpq,-b)
        else:
            if gpq.__len__()<3:
                dea+=1000
            else:
                c,d,f=pop(gpq),pop(gpq),pop(gpq)
                dea+=-f
                push(gpq,c)
                push(gpq,d)
                push(gpq,f)

    if dea==guu:
        print("우열을 가릴 수 없음")
        return 0
    print("소수의 신 갓대웅" if dea>guu else "소수 마스터 갓규성")
        
main()
