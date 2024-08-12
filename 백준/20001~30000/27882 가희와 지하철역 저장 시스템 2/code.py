input=open(0).readline
INF=float('inf')

def floyd(gr,M):
	for i in range(M):
		for j in range(M):
			for k in range(M):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])
	return gr
	
#important function
def process(R_node_name,station_name,request_node_db,cache_node_db,h):
    p = request_node_db[R_node_name]['short_node_name']
    if station_name in cache_node_db[p]:
        return request_node_db[R_node_name]['short_distance']*2
    return 0
	
def main():
    #init
    N,M,H,Q=map(int,input().split())
    stations=set()
    for _ in range(N):
        stations.add(input().strip())
    node_info={}
    bucket=[]
    cache=[]
    request=[]
    gr=[[INF]*(M)for _ in range(M)]
    for i in range(M):gr[i][i]=0
    
    #node informations input
    for i in range(M):
        node_name,node_type=input().strip().split()
        if node_type=='B':
            bucket.append(node_name)
        elif node_type=='C':
            cache.append(node_name)
        else:
            request.append(node_name)
        node_info[node_name]=i
        node_info[i]=node_name
    
    #graph input
    for _ in range(int(input())):
        node1,node2,rt = input().strip().split()
        node1_index,node2_index=node_info[node1],node_info[node2]
        gr[node1_index][node2_index]=int(rt)
        gr[node2_index][node1_index]=int(rt)
    gr=floyd(gr,M)
    request_node_db={}
    cache_node_db={o:{} for o in cache}
    
    #each request node minimum distance to cache node
    for n in request:
        j=node_info[n]
        k=INF
        b=1e9+1
        for p in cache:
            i=node_info[p]
            rk=gr[j][i]
            if (rk<k)or (rk==k and int(p)<int(b)):
                b=node_info[i]
                k=rk
        request_node_db[n]={'short_node_name':b,'short_distance':k} 
    
    #processing quarry
    for _ in range(Q):
        p_node_name,station_name=input().strip().split()
        ans=process(p_node_name,station_name,request_node_db,cache_node_db,H)
        print(ans)

main()

#cache_node_db structure
#cache_node_name:name(str)
#db={}(dict)
#{name:db}
#
#
