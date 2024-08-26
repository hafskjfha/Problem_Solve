from collections import deque,defaultdict
input=open(0).readline
INF=float('inf')
def create_tree(D,P):
    gr=defaultdict(list)
    nodes=2**D-1
    for i in range(1,nodes+1):
        left=2*i
        right=2*i+1
        if left<=nodes and (i,left) not in P:
            gr[i].append(left)
        if right<=nodes and (i,right)not in P:
            gr[i].append(right)
    return gr
def bfs(gr,D,U,T):
    V=[INF]*2**D
    q=deque([[1,U]])
    V[1]=0
    j=0
    while q:
        node,move_t=q.popleft()
        if not gr[node]:
            j=max(V[node],j)
        for next_n in gr[node]:
            if V[next_n]!=INF:continue
            if len(gr[node])==2:
                q.append([next_n,move_t+T])
                V[next_n]=move_t+T+V[node]
            else:
                q.append([next_n,move_t])
                V[next_n]=move_t+V[node]
    return j
    
def dfs_path(graph):
    global last_visited_node
    path = []
    visited = set()
    last_visited_node=1
    def dfs(node):
        global last_visited_node
        visited.add(node)
        path.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                last_visited_node=neighbor
                dfs(neighbor)
                path.append(node)
    dfs(1)
    for i in range(len(path)-1,-1,-1):
    	if path[i]!=last_visited_node:
    		path.pop()
    	else:
    		break
    return len(path)-1

def main():
    D,N,U,T=map(int,input().split())
    if D==1:
        print(':blob_twintail_thinking:')
        return
    P=set(tuple(map(int, input().split())) for _ in range(N))
    gr=create_tree(D,P)
    tb=bfs(gr,D,U,T)
    pb=dfs_path(gr)*U
    if pb==tb:
    	print(':blob_twintail_thinking:')
    	return
    print(':blob_twintail_aww:'if tb<pb else ':blob_twintail_sad:')
main()
