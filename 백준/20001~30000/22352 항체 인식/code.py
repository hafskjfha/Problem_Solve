import sys
from collections import deque
input=sys.stdin.readline
H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
B=[list(map(int,input().split())) for _ in range(H)]
def bfs(S):
	q,c,o=deque([S]),B[j][i],A[j][i]
	while q:
		x,y=q.popleft()
		if A[y][x]==c:continue
		A[y][x]=c
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<W and 0<=dy<H and A[dy][dx]==o:
				q.append((dx,dy))
for i in range(W):
	for j in range(H):
		if A[j][i]!=B[j][i]:
			bfs((i,j))
			break
	else:
		continue
	break
if A==B:print('YES')
else:print('NO')
