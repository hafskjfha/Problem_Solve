from collections import deque
M,W,L=map(int,input().split())
T=deque(list(map(int,input().split())))
E=deque()
nL=0
C=0
fl=False
while T:
	for _ in range(len(E)):
		r,x=E.popleft()
		if x+1>W:
			nL-=r
			continue
		E.append((r,x+1))
	if T[0]+nL<=L:
		K=T.popleft()
		nL+=K
		fl=True
	if fl:
		E.append((K,1))
		fl=False
	C+=1
if E:
	r,x=E.pop()
	C+=W-x+1
print(C)
