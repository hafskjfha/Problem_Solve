import sys
from collections import deque
input=sys.stdin.readline
def bfs(S):
	q=deque([S])
	while q:
		x,y=q.popleft()
		if m[y][x]==7:
			continue
		m[y][x],a[y][x]=7,'S'
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and m[dy][dx]=='T':
				q.append((dx,dy))
while 1:
	W,H=map(int,input().split())
	if (W,H)==(0,0):
		break
	a=[['.']*W for _ in range(H)]
	m=[list(input().strip()) for _ in range(H)]
	for i in range(W):
		for j in range(H):
			if m[j][i]=='S':
				bfs((i,j))
			elif m[j][i]=='T':
				a[j][i]='T'
	for b in a:
		for c in b:
			print(c,end="")
		print()
