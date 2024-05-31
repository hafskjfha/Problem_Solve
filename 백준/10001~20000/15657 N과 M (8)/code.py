import sys
n,m=list(map(int,input().split()))
nums=sorted(list(map(int,input().split())))
s=[]
def bac():
	if len(s)==m:
		sys.stdout.write(' '.join(map(str, s)) + '\n')
		return
	for i in nums:
		if not s or i>=s[-1]:
			s.append(i)
			bac()
			s.pop()
bac()
