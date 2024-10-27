import os,heapq
hpush=heapq.heappush
hpop=heapq.heappop
class double_pq:
    def __init__(self) -> None:
        self.min_heap:list[tuple[int,int]]=[]
        self.max_heap:list[tuple[int,int]]=[]
        self.c:dict[tuple[int,int],bool]={}
    def push(self,k:int,p:int)->None:
        self.c[(p,k)]=False
        hpush(self.max_heap,(-p,k))
        hpush(self.min_heap,(p,k))
    def min_pop(self) -> int:
        while self.min_heap and self.c[self.min_heap[0]]:
            hpop(self.min_heap)
        if not self.min_heap:
            return 0
        p=self.min_heap[0]
        self.c[p]=True
        return p[1]

    def max_pop(self) -> int:
        while self.max_heap and self.c[(-self.max_heap[0][0],self.max_heap[0][1])]:
            hpop(self.max_heap)
        if not self.max_heap:
            return 0
        k,p=self.max_heap[0][1],-self.max_heap[0][0]
        self.c[(p,k)]=True
        return k

def main():
    input=os.read(0,os.stat(0).st_size).decode().split('\n').__iter__().__next__
    print=os.write
    exit=os._exit
    OK=os.EX_OK
    encode=str.encode
    pq=double_pq()
    while 1:
        C,*k=map(int,input().split())
        if C==0:exit(OK)
        elif C==1:
            pq.push(*k)
        elif C==2:
            print(1,encode(f'{pq.max_pop()}\n'))
        else:
            print(1,encode(f'{pq.min_pop()}\n'))



main()
