def main():
    input=open(0).readline
    print=open(1,'w').write
    from collections import deque
    F,S,G,U,D=map(int,input().split())
    S,G=S-1,G-1
    V=[0]*F
    V[S]=1
    q=deque([S])
    while q:
        x=q.popleft()
        if x==G:
            print(str(V[x]-1))
            return
        for dx in (x+U,x-D):
            if 0<=dx<F and not V[dx]:
                V[dx]=V[x]+1
                q.append(dx)
    print('use the stairs')
        
main()
