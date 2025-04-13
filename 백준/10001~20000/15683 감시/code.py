def cctv_check(office,n,m,x,y,kind,mode): 
    def right():
        for i in range(x+1,m):
            if office[y][i]=="6":
                break
            
            if office[y][i]=="0":
                office[y][i]="#"
    def down():
        for i in range(y+1,n):
            if office[i][x] == "6":
                break
            
            if office[i][x] == "0":
                office[i][x]="#"
    def left():
        for i in range(x-1,-1,-1):
            if office[y][i] == "6":
                break
            
            if office[y][i] == "0":
                office[y][i]="#"
    def up():
        for i in range(y-1,-1,-1):
            if office[i][x] == "6":
                break
            
            if office[i][x] == "0":
                office[i][x]="#"
    match kind:
        case 1:
            if mode == 1:
                right()
            
            elif mode == 2:
                down()
            
            elif mode == 3:
                left()
            
            elif mode == 4:
                up()
        case 2:
            if mode == 1:
                left()
                right()
            
            elif mode == 2:
                down()
                up()
        case 3:
            if mode == 1:
                up()
                right()
            
            elif mode == 2:
                right()
                down()
                        
            elif mode == 3:
                down()
                left()
            
            elif mode == 4:
                left()
                up()
        case 4:
            if mode == 1:
                up()
                right()
                down()
            
            elif mode == 2:
                right()
                down()
                left()
            
            elif mode == 3:
                down()
                left()
                up()
            
            elif mode == 4:
                left()
                up()
                right()
        case 5:
            up()
            right()
            down()
            left()
    return office

def blind_check(office):
    return sum(row.count("0") for row in office)


def expand_type(x, y, t):
    if t == 2:
        return [(x, y, t, i) for i in range(1, 3)]
    elif t == 5:
        return [(x, y, t, 1)]         
    elif t in [1, 3, 4]:
        return [(x, y, t, i) for i in range(1, 5)]


def main():
    from itertools import product
    n,m=map(int,input().split())
    office=[]
    cctvs=[]
    ans=float('inf')
    for y in range(n):
        t=input().split()
        office.append(t)
        for x in range(m):
            if t[x] in "12345":
                cctvs.append((x,y,int(t[x])))
    
    for alls in product(*[expand_type(x, y, t) for (x, y, t) in cctvs]):
        copy_office = copy_office = [row[:] for row in office]
        for x,y,t,mode in alls:
            copy_office = cctv_check(copy_office,n,m,x,y,t,mode)
        
        ans = min(ans,blind_check(copy_office))
    
    print(ans)

main()