import sys
n,m = list(map(int,input().split()))
s = []
def bac():
    if len(s)==m:
        sys.stdout.write(' '.join(map(str, s)) + '\n')
        return
    for i in range(1,n+1):
        if not s or i>=s[-1]:
            s.append(i)
            bac()
            s.pop()
bac()
