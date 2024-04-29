import sys
j = int(sys.stdin.readline())
N = []
for _ in range(j):
    N.append(int(sys.stdin.readline().strip()))
N.sort()
for _ in N:
    print(_)
    
