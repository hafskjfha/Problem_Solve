#pypy3
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=[list(input().strip()) for _ in range(N)]
def dfs(x,y,v,c):
	global K
	K=max(K,c)
	for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
		if 0<=dx<M and 0<=dy<N :
			if not v[ord(A[dy][dx])-65]:
				v[ord(A[dy][dx])-65]=1
				dfs(dx,dy,v,c+1)
				v[ord(A[dy][dx])-65]=0
vi=[0]*26
K=1
vi[ord(A[0][0])-65]=1
dfs(0,0,vi,1)
print(K)
