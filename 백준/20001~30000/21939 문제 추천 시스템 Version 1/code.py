import heapq,os
hpush=heapq.heappush
hpop=heapq.heappop

class double_pq:
    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        self.p_list={}
    def push(self,id,v):
        hpush(self.min_heap,(v,id))
        hpush(self.max_heap,(-v,-id))
        self.p_list[id]=v
    def remove(self,id):
        self.p_list[id]=None
        while self.min_heap and self.p_list[self.min_heap[0][1]]!=self.min_heap[0][0]:
            hpop(self.min_heap)
        while self.max_heap and self.p_list[-self.max_heap[0][1]]!=-self.max_heap[0][0]:
            hpop(self.max_heap)
    def get_min(self):
        while self.min_heap and self.p_list[self.min_heap[0][1]]!=self.min_heap[0][0]:
            hpop(self.min_heap)
        return self.min_heap[0][1]
    def get_max(self):
        while self.max_heap and self.p_list[-self.max_heap[0][1]]!=-self.max_heap[0][0]:
            hpop(self.max_heap)
        return -self.max_heap[0][1]
def main():
    input=os.read(0,os.stat(0).st_size).decode().split('\n').__iter__().__next__
    print=os.write
    encode=str.encode
    pq=double_pq()
    for _ in range(int(input())):
        id,h=map(int,input().split())
        pq.push(id,h)
    for _ in range(int(input())):
        c,*v=input().split()
        match c:
            case "add":
                pq.push(*map(int,v))
            case "recommend":
                if v[0]=='1':
                    print(1,encode(f'{pq.get_max()}\n'))
                else:
                    print(1,encode(f'{pq.get_min()}\n'))
            case "solved":
                pq.remove(int(v[0]))
    os._exit(os.EX_OK)
    
main()
