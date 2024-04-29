import sys
input=sys.stdin.readline
N = int(input())
s = list(map(int,input().split()))
o = 0
for i in s:
	if i >1:			
			for j in range(2,int(i**(1/2))+1):
				u = i%j
				if u==0:
					break
			else:
					o += 1
print(o)
