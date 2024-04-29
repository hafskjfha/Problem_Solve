import sys
from collections import deque
input = sys.stdin.readline
def bfs(c,d):
	q = deque([(c,d)])
	while q:
		coo = q.popleft()
		x,y=coo[0],coo[1]
		info = m[y][x]
		if info != '*' and info != '#':
			m[y][x] = '#'
			ti = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
			for o,p in ti:
				if o > -1 and o < W and p > -1 and p < H and m[p][o] == '@':
					q.append((o,p))
	return 
		

while True:
	H,W = map(int,input().split())
	if W==0 and H==0:
		break
	m=[]
	su=0
	for _ in range(H):
		m.append(list(input()))
	for i in range(W):
		for j in range(H):
			if m[j][i] == '@':
				bfs(i,j)
				su += 1
	print(su)
