n,m = list(map(int,input().split()))
s = []
def bac():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1):
        if i not in s and (not s or i>s[-1]):
            s.append(i)
            bac()
            s.pop()
bac()
