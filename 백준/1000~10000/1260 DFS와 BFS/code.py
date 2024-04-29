from collections import deque
import sys
input=sys.stdin.readline
class Graph:
	def __init__(self):		
		self.adj_list={}
		self.visited=set()
	def add_edge(self,i1,i2):
		if i1 not in self.adj_list:
			self.adj_list[i1]=[]
		self.adj_list[i1].append(i2)
		if i2 not in self.adj_list:
			self.adj_list[i2]=[]
		self.adj_list[i2].append(i1)
	def sort_edges(self): 
		for node in self.adj_list: 
			self.adj_list[node].sort()
	def dfs(self,node):
		if node not in self.visited:
			self.visited.add(node)
			print(node,end=" ")
			for ne in self.adj_list.get(node,[]):
				self.dfs(ne)
	def bfs(self,snode):
		self.visited=set()
		q=deque([snode])
		while q:
			node=q.popleft()
			if node not in self.visited:
				self.visited.add(node)
				print(node,end=" ")
				for ne in self.adj_list.get(node,[]):
					if ne not in self.visited:
						q.append(ne)
N,M,V=map(int,input().split())
graph=Graph()
for _ in range(M):
	a,b=map(int,input().split())
	graph.add_edge(a,b)
graph.sort_edges()
graph.dfs(V)
print()
graph.bfs(V)

		
