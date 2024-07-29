import sys
from copy import deepcopy
from collections import deque
input=sys.stdin.readline
copy=deepcopy
N,Q=map(int,input().split())
P=[input().strip()for _ in range(Q)]
back=deque()
front=deque()
now=None
for p in P:
    if p[0]=='B':
        if back:
            front.appendleft(now)
            now=back.pop()
        else:
            continue
    elif p[0]=='F':
        if front:
            back.append(now)
            now=front.popleft()
        else:
            continue
    elif p[0]=='A':
        front=deque()
        if now !=None:
            back.append(now)
        now=p[2:]
    elif p[0]=='C':
        tempback=deque()
        end=None
        for i in back:
            if i!=end:
                end=i
                tempback.append(i)
        back=copy(tempback)
print(now)
[print(back.pop(),end=' ')for _ in range(len(back))]if back else print(-1,end='')
print()
[print(front.popleft(),end=' ')for _ in range(len(front))]if front else print(-1)
