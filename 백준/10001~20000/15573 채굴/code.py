def bfs(mine,n,m,d,k):
    from collections import deque
    s=[(i,0) for i in range(m) if mine[0][i]<=d]
    for i in range(1,n):
        if mine[i][0]<=d:
            s.append((0,i))
        if mine[i][m-1]<=d:
            s.append((m-1,i))
    q=deque(s)
    c=len(q)
    v=[[0]*m for _ in range(n)]
    for x,y in q:
        v[y][x]=1
        
    while q:
        x,y=q.popleft()
        for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=dx<m and 0<=dy<n and mine[dy][dx]<=d and not v[dy][dx]:
                v[dy][dx]=1
                c+=1
                if c>=k:
                    return True
                q.append((dx,dy))
                
    return c>=k
    
def main():
    import sys
    input=sys.stdin.readline
    n,m,k=map(int,input().split())
    ans=0
    mine=[[*map(int,input().split())] for _ in range(n)]
    left,right=1,1000000
    while left<=right:
        mid=(left+right)//2
        if bfs(mine,n,m,mid,k):
            ans=mid
            right=mid-1
        else:
            left=mid+1
    print(ans)
main()
        