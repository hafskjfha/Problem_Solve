import heapq
def dijkstra(K,E,N,L,C,gr):
	d=[float('inf')]*(N+1)
	d[K]=0
	heap=[[0,K]]
	while heap:
		w,v=heapq.heappop(heap)
		if d[v]<w:continue
		for nw,nv in gr[v]:
			if d[nv]>w+nw and nw<=L:
				d[nv]=w+nw
				heapq.heappush(heap,[d[nv],nv])
	return d[E]<=C
def main():
	input=open(0).readline
	N,M,A,B,C=map(int,input().split())
	gr=[[]for _ in range(N+1)]
	mp=set()
	for _ in range(M):
		d,e,f=map(int,input().split())
		gr[d].append([f,e])
		gr[e].append([f,d])
		mp.add(f)
	mp=sorted([*mp])
	start,end=0,len(mp)-1
	ans=float("inf")
	while start<=end:
		mid=(start+end)//2
		if dijkstra(A,B,N,mp[mid],C,gr):
			end=mid-1
			ans=mp[mid]
		else:
			start=mid+1
	print(ans if ans!=float("inf")else -1)

main()
