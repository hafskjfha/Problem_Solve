from collections import deque
input=open(0).readline
def bfs(start_nodes,mode,node_info,nodes,time):
    q=deque([*start_nodes])
    p=('S','W')if mode=='m'else ('S')
    obj_count=0
    visit=set()
    while q:
        node=q.popleft()
        visit.add(node)
        obj_count+=1
        del_check=[]
        for ref_id,next_node,connect,madetime in node_info[node]:
            if next_node not in visit and connect in p:
                if next_node in nodes and nodes[next_node]<madetime:
                    q.append(next_node)
                    visit.add(next_node)
                else:
                    del_check.append((ref_id,next_node,connect,madetime))
        for ref_id,del_node,connect,madetime in del_check:
            node_info[node].remove((ref_id,del_node,connect,madetime))
    del_nodes=[]
    for i in node_info.keys():
        if i not in visit:
            del_nodes.append(i)
            del nodes[i]
    for i in del_nodes:
        del node_info[i]
    print(len(nodes))
    return node_info,nodes
    
def main():
    O,E=map(int,input().split())
    node_info={}
    nodes={}
    root_nodes=set()
    ref_ids={}
    for _ in range(O):
        id,is_root=input().strip().split()
        if is_root=="ROOT":
            root_nodes.add(id)
        node_info[id]=set()
        nodes[id]=-1
    for t in range(E):
        cal,*info=input().strip().split()
        if cal=="MADE":
            id,is_root=info
            if is_root=="ROOT":
                root_nodes.add(id)
            node_info[id]=set()
            nodes[id]=t 
        elif cal=="ADD":
            ref_id,id1,connect,id2=info
            k='S'if connect=='=>'else 'W'
            ref_ids[ref_id]=[id1,id2,k,t]
            node_info[id1].add((ref_id,id2,k,t))
        elif cal=='REMOVE':
            del_ref_id=info[0]
            id1,id2,r,maketime=ref_ids[del_ref_id]
            node_info[id1].remove((del_ref_id,id2,r,maketime))
        elif cal=='M':
            node_info,nodes=bfs(root_nodes,'M',node_info,nodes,t)
        elif cal=='m':
            node_info,nodes=bfs(root_nodes,'m',node_info,nodes,t)
main()
