import sys
input=sys.stdin.readline
while True:
	N=list(map(int,input().split()))
	if N[0]==0 and N[1]==0 and N[2]==0:
		break
	Z=max(N)
	N.remove(Z)
	if N[0]**2 + N[1]**2 == Z**2:
		print('right')
	else:
		print('wrong')
