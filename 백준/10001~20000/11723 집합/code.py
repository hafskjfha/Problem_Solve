import sys
input=sys.stdin.readline
M=int(input())
S=set()
for _ in range(M):
	w=input().strip().split()	
	if w[0]=='add':
		S.add(int(w[1]))
	elif w[0]=='remove':
		if int(w[1]) in S:
			S.remove(int(w[1]))
	elif w[0]=='check':
		if int(w[1]) in S:
			print(1)
		else:
			print(0)
	elif w[0]=='toggle':
		if int(w[1]) in S:
			S.remove(int(w[1]))
		else:
			S.add(int(w[1]))
	elif w[0]=='all':
		S=set(range(1,21))
	elif w[0]=='empty':
		S=set()
