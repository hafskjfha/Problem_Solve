from heapq import heappush,heappop
pq=[]
input=open(0).readline
push=heappush
pop=heappop
S=0 
for _ in range(int(input())):
    push(pq,int(input()))
while len(pq)>1:
    k=pop(pq)+pop(pq)
    S+=k
    push(pq,k)
print(S)
