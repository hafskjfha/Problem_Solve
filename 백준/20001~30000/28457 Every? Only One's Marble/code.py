from collections import deque
input=open(0).readline
def sol(N,now_money,salary,turn_number,gold_keys,board,dice_q,dosi):
    i=-1
    now_position=0
    buy_dosi=0
    donation=0
    pp=True
    while i<turn_number:
        if pp:
            i+=1
            if i>=turn_number:
                return 1 if buy_dosi==dosi else 0
            a,b=dice_q[i]
            now_position+=a+b
            
        now_money+=(now_position//(4*N-4))*salary
        now_position%=4*N-4
        temp=board[now_position]
        if temp in ('start','island','welfare','universe'):
            if temp=='island':
                for _ in range(3):
                    i+=1
                    if i>=turn_number:
                        return (1 if buy_dosi==dosi else 0)
                    a,b=dice_q[i]
                    if a==b:
                        break
            elif temp=='welfare':
                now_money+=donation
                donation=0
            elif temp=='universe':
                now_money+=salary
                now_position=0
        
        elif temp=='G':
            k,x=gold_keys.popleft()
            if k==1:
                now_money+=x
                gold_keys.append([k,x])
            elif k==2:
                now_money-=x
                if now_money<0:return 0
                gold_keys.append([k,x])
            elif k==3:
                now_money-=x
                if now_money<0:return 0
                donation+=x
                gold_keys.append([k,x])
            elif k==4:
                now_position+=x
                if now_position>4*N-5:
                    now_money+=salary
                    now_position-=4*N-4
                pp=False
                gold_keys.append([k,x])
                continue
            
        else:
            if temp!=-1 and now_money>=temp:
                buy_dosi+=1
                now_money-=temp
                board[now_position]=-1
                
        pp=True
    if dosi==buy_dosi:
        return 1
    return 0
    
    
def main():
    N,S,W,G=map(int,input().split())
    board=[0]*(4*N-4)
    gold_keys=deque([])
    for _ in range(G):
        k,j=map(int,input().split())
        gold_keys.append([k,j])
    board[0]='start'
    board[N-1]='island'
    board[2*N-2]='welfare'
    board[3*N-3]='universe'
    i=1
    dosi=0
    while i < 4*N-4:
        if i in (N-1,2*N-2,3*N-3):i+=1    
        info,*j=input().strip().split()
        if info=='G':
            board[i]=info
        else:
            board[i]=int(j[0])
            dosi+=1
        i+=1
    
    dice_q=[]
    I=int(input())
    for _ in range(I):
        a,b=map(int,input().split())
        dice_q.append([a,b])
    print('WIN'if sol(N,S,W,I,gold_keys,board,dice_q,dosi)else'LOSE')
    
main()
