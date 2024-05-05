T=int(input())
def bfs(q):
	c=0	
	while q:
		x,y=q.pop(0)
		if b[y][x]==7:continue
		b[y][x]=7
		for dx,dy in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
			if 0<=dx<N and 0<=dy<N and b[dy][dx]=='-' and (dx,dy) not in q:
				q.append((dx,dy))
				c+=1
	return c
for _ in range(T):
	N=int(input())
	b,s,c=[list(input().strip()) for _ in range(N)],[],0
	for i in range(N):
		for j in range(N):
			if b[j][i]=='w':s.append((i,j))
	c+=bfs(s);print(c)
