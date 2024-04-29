import sys
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
c=list(map(int,input().split()))
ac = list(combinations(c,3))
s=[]
for t in ac:
	s.append(sum(t))	
s = [u for u in s if u<=M]
print(max(s))
