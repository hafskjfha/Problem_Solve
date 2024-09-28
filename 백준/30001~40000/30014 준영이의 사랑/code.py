from collections import deque
N=int(input())
ans=0
K=sorted([*map(int,input().split())],key=lambda x:-x)
b=deque()
for i in range(N):
	b.append(K[i])if i%2 else b.appendleft(K[i])
for i in range(N-1):
	ans+=b[i]*b[i+1]
ans+=b[0]*b[-1]
print(ans)
print(*b)
