import sys
input=sys.stdin.readline
N = int(input())
k=[]
for _ in range(N):
	h = input().strip().split()	
	k.append((int(h[0]),h[1]))
k.sort(key=lambda x:x[0])
for s in k:
	print(s[0],s[1])
