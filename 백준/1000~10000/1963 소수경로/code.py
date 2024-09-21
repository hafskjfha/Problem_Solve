from collections import deque
def prime_check():
    is_prime=[1]*10001
    is_prime[0]=is_prime[1]=0
    for i in range(2,int(10000**0.5)+1):
        if is_prime[i]:
            for j in range(i*2,10001,i):
                is_prime[j]=0
    return is_prime
def bfs(s,e,prime):
    def nq(num,p,r):
        return num-(num//10**(4-p)%10)*10**(4-p)+r*10**(4-p)
    q=deque([(s,0)])
    V=set([s])
    while q:
        x,t=q.popleft()
        if x==e:return t
        for i in range(1,5):
            for j in range(10):
                if i==1 and j==0:continue
                y=nq(x,i,j)
                if prime[y] and y not in V:
                    q.append((y,t+1))
                    V.add(y)
def main():
    prime=prime_check()
    for _ in range(int(input())):
        print(bfs(*map(int,input().split()),prime))
main()
            
