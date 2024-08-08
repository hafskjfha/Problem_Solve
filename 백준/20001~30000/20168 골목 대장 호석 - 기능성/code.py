input=open(0).readline
ans=10001
N,M,A,B,C=map(int,input().split())
gr=[[]for _ in range(N+1)]
for _ in range(M):
	D,E,F=map(int,input().split())
	gr[D].append([E,F])
	gr[E].append([D,F])
def bac(n,v,md,p):
	global ans
	if n==B:
		ans=min(ans,md)
		return
	for nn,k in gr[n]:
		if nn not in v and p+k<=C:
			v.add(nn)
			bac(nn,v,max(md,k),p+k)
			v.remove(nn)
bac(A,set([A]),0,0)
print(ans if ans!=10001 else -1)
