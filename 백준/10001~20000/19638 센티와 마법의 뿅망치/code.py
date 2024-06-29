import heapq as h
import sys
ip=sys.stdin.readline
N,H,T=map(int,ip().split())
q=[]
for i in range(1,N+1):
	h.heappush(q,-int(ip()))
def v():
	c=0
	for i in range(T):
		if (j:=-h.heappop(q))>=H and j!=1:
			h.heappush(q,-(j//2))
			c+=1
		elif j==1:
			h.heappush(q,-1)
			break
		else:return print(f'YES\n{c}')
	print(f'NO\n{j}')if (j:=-h.heappop(q))>=H else print(f'YES\n{c}')
v()
