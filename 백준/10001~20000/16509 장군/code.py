from collections import deque
R1,C1=map(int,input().split())
R2,C2=map(int,input().split())
m=[[0]*9 for _ in range(10)]
m[R1][C1],m[R2][C2]=1,9
def bfs():
	q=deque([(C1,R1,0)])	
	while q:
		x,y,di=q.popleft()
		if m[y][x]==2:continue
		if (x,y)==(C2,R2):return di	
		for dx,dy,r in [(x-2,y-3,1),(x+2,y-3,2)]:
			if 0<=dx<9 and 0<=dy<10 and m[y-1][x]!=9:
				if r==1 and m[y-2][x-1]!=9:
					q.append((dx,dy,di+1))
				elif r==2 and m[y-2][x+1]!=9:
					q.append((dx,dy,di+1))
		for dx,dy,r in [(x-3,y-2,1),(x-3,y+2,2)]:
			if 0<=dx<9 and 0<=dy<10 and m[y][x-1]!=9:
				if r==1 and m[y-1][x-2]!=9:
					q.append((dx,dy,di+1))
				elif r==2 and m[y+1][x-2]!=9:
					q.append((dx,dy,di+1))
		for dx,dy,r in [(x-2,y+3,1),(x+2,y+3,2)]:
			if 0<=dx<9 and 0<=dy<10 and m[y+1][x]!=9:
				if r==1 and m[y+2][x-1]!=9:
					q.append((dx,dy,di+1))
				elif r==2 and m[y+2][x+1]!=9:
					q.append((dx,dy,di+1))
		for dx,dy,r in [(x+3,y-2,1),(x+3,y+2,2)]:
			if 0<=dx<9 and 0<=dy<10 and m[y][x+1]!=9:
				if r==1 and m[y-1][x+2]!=9:
					q.append((dx,dy,di+1))
				elif r==2 and m[y+1][x+2]!=9:
					q.append((dx,dy,di+1))
	return -1
print(bfs())
