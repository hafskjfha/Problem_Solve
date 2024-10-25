import heapq,os
from collections import defaultdict
hpush=heapq.heappush
hpop=heapq.heappop
class min_pq:
    def __init__(self):
        self.min_heap=[]
        self.element_dict=defaultdict(int)
    def remove(self,v):
        self.element_dict[v]-=1
        while self.min_heap and self.element_dict[self.min_heap[0]]==0:
            hpop(self.min_heap)
    def push(self,v):
        if self.element_dict[v]:
            self.element_dict[v]+=1
        else:
            hpush(self.min_heap,v)
            self.element_dict[v]+=1
    def get_min(self):
        while self.min_heap and self.element_dict[self.min_heap[0]]==0:
            hpop(self.min_heap)
        return self.min_heap[0]
def main():
    input=open(0).readline
    input=os.read(0,os.stat(0).st_size).decode().split('\n').__iter__().__next__
    print=os.write
    exit=os._exit
    OK=os.EX_OK
    encode=str.encode
    for _ in range(int(input())):
        N,S=map(int,input().split())
        stack=[]
        pq=min_pq()
        for _ in range(N):
            km=float('inf')
            X=int(input())
            if X>0:
                stack.append(X)
                pq.push(X)
            else:
                ch=False
                if km==float('inf') and stack:
                    km=pq.get_min()
                if not stack or km>-X:
                    S+=X
                else:
                    while stack:
                        if X>=0:break
                        k=stack.pop()
                        if k==km:
                            ch=True
                        pq.remove(k)
                        X+=k
                    S+=X   
                    if ch and stack:
                        km=pq.get_min()
                    elif ch:
                        km=float('inf')
        print(1,encode(f'{S} {sum(stack)}\n'))
    exit(OK)


main()
