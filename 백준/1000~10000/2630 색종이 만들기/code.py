import sys
input=sys.stdin.readline
N=int(input())
P=[list(input().strip().split()) for _ in range(N)]
W,B=0,0
def cut(K,r,c):
	global W,B
	if K==0:
		if P[c][r]=='0':W+=1 
		else:B+=1
		return
	a=P[c][r]
	for i in range(r,r+K):
		for j in range(c,c+K):
			if P[j][i]!=a:
				break
		else:
			continue
		break
	else:
		if a=='0':W+=1 
		else:B+=1
		return
	S=K//2
	cut(S,r+S,c+S)
	cut(S,r,c+S)
	cut(S,r+S,c)
	cut(S,r,c)
cut(N,0,0)
print(W,B,sep='\n')
