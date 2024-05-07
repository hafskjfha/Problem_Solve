import sys
from collections import deque
input=sys.stdin.readline
R,C=map(int,input().split())
ma=[list(input().strip()) for _ in range(R)]
HR,HC=map(int,input().split());logs=list(input().strip())
vi,anw,cux,cuy=[[False]*C for _ in range(R)],[['#']*C for _ in range(R)],HC-1,HR-1
def bfs(S):
	q=deque([S])
	while q:
		x,y = q.popleft()
		if vi[y][x]:
			continue
		vi[y][x],anw[y][x],info=True,'.',ma[y][x]
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<C and 0<=dy<R and ma[dy][dx]==info and not vi[dy][dx]:q.append((dx,dy))
for log in logs:
	if log=='W' and anw[cuy][cux]=="#":bfs((cux,cuy))
	elif log=='U':cuy-=1
	elif log=='D':cuy+=1
	elif log=='L':cux-=1
	elif log=='R':cux+=1
anw[cuy][cux]='.'
for dx,dy in [(cux+1,cuy),(cux-1,cuy),(cux,cuy-1),(cux,cuy+1)]:
	if 0<=dx<C and 0<=dy<R and anw[dy][dx]=='#':anw[dy][dx]='.'
for i in anw:
	for j in i:
		print(j,end='')
	print()
