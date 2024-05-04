from collections import deque
import sys
input=sys.stdin.readline
H,W=map(int,input().split())
def bfs(S):
	q=deque([(S)])
	while q:
		x,y=q.popleft()
		if f[y][x]==-1:
			continue
		f[y][x]=-1
		for dx,dy in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
			if 0<=dx<W and 0<=dy<H and f[dy][dx]>0:
				q.append((dx,dy))
f,c=[list(map(int,input().split())) for _ in range(H)],0
for i in range(W):
	for j in range(H):
		if f[j][i]>0:
			bfs((i,j))
			c+=1
print(c)
