import sys
input = sys.stdin.readline
S=list(input().strip())
S.sort(reverse=True)
print(''.join(S))
