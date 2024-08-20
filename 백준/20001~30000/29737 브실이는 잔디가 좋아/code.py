input=open(0).readline
INF=float('inf')
def pro(cal,W,name):
    fail_streak=0
    max_streak=0
    use_streak_freeze=0
    start_date=INF
    temp_max_streak=0
    temp_start_date=INF
    temp_use_streak_freeze=0
    t_j=0
    k=1
    cke=[]
    for i in range(W):
        for j in range(7):
            if cal[j][i]=='O':
                if temp_max_streak==0:
                    temp_start_date=k
                temp_max_streak+=1
                temp_use_streak_freeze+=t_j
                t_j=0
            elif cal[j][i]=='F':
                if temp_max_streak:
                    t_j+=1
            else:
                
                cke.append([-temp_max_streak,temp_use_streak_freeze,temp_start_date])
                t_j=0
                temp_max_streak=0
                temp_use_streak_freeze=0
                fail_streak+=1
            k+=1
    cke.append([-temp_max_streak,temp_use_streak_freeze,temp_start_date])
    cke.sort()
    
    return [*cke[0],fail_streak,name]
    
def main():
    N,W=map(int,input().split())
    rank=[]
    for _ in range(N):
        name=input().strip()
        temp=[list(input().strip())for _ in range(7)]
        rank.append(pro(temp,W,name))
    rank.sort()
    i=1
    print(f'{i}. {rank[0][4]}')
    for j in range(1,N):
        if rank[j-1][:4]!=rank[j][:4]:
            i+=1
        print(f'{i}. {rank[j][4]}')
        
main()
