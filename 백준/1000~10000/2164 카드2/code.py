from collections import deque
N = int(input())
j=list(range(1,N+1))
d = deque(j)
while True:
	if len(d) ==1 :	break
	d.popleft()
	d.append(d.popleft())
print(d[0])
