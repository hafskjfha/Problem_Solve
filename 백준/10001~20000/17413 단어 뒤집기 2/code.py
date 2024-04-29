import sys
from collections import deque
input = sys.stdin.readline
S = list(input().strip())
de = deque()
l,u = False,False
o = deque()
for c in S:
	if c == "<":
		u=False
		while o:
			de.append(o.pop())
		l = True
		de.append(c)
	elif c == ">":
		l = False
		de.append(c)
	elif l:
		de.append(c)
	elif c==" ":
		u=False
		if l:
			continue
		while o:
			de.append(o.pop())
		de.append(c)
	elif u:
		o.append(c)
	
	else:
		o.append(c)
		u=True
while o:
	de.append(o.pop())
j="".join(de)
print(j)
