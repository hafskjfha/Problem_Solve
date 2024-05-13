import sys
from collections import deque
input=sys.stdin.readline
m,a=[list(map(int,input().split())) for _ in range(5)],0
r,c=map(int,input().split())
def bfs(S,t):
	q,v=deque([S]),[[0]*5 for _ in range(5)]
	while q:
		x,y,d=q.popleft()
		if v[y][x]:continue
		if m[y][x]==t:return x,y,d
		v[y][x]=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<5 and 0<=dy<5 and m[dy][dx]!=-1 and not v[dy][dx]:q.append((dx,dy,d+1))
	print(-1)
	sys.exit()
for i in range(1,7):
	c,r,b=bfs((c,r,0),i)
	a+=b
print(a)
