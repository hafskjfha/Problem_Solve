import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def bfs(c,d):
	q = deque([(c,d)])
	while q:
		coo = q.popleft()
		x,y=coo[0],coo[1]
		info = farm[y][x]
		if info != 0 and info != 2:
			farm[y][x] = 2
			ti = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
			for o,p in ti:
				if o > -1 and o < M and p > -1 and p < N and farm[p][o] == 1:
					q.append((o,p))
	return 1

for _ in range(T):
	jiro=0
	M,N,K=map(int,input().split())
	farm = [[0]*M for _ in range(N)]
	for __ in range(K):
		a,b = map(int,input().split())
		farm[b][a] = 1
	for i in range(M):
		for j in range(N):
			if farm[j][i] == 1:
				bfs(i,j)
				jiro += 1
	print(jiro)
		
	
