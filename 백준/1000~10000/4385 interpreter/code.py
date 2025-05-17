def main():
    ans=0
    registers=[0]*10
    ram=[*map(int,open(0))]+[0]*999
    ads=0
    
    while 1:
        cmd=ram[ads]
        cmd_c=cmd//100
        d=(cmd-cmd_c*100-cmd%10)//10
        n=cmd%10
        
        match cmd_c:
            case 0:
                if registers[n]:
                    ads=registers[d]
                else:
                	ads+=1
                
            case 1:
                print(ans+1)
                return
            case 2:
                registers[d]=n
                ads+=1
                
            case 3:
                registers[d]=(registers[d]+n)%1000
                ads+=1
                
            case 4:
                registers[d]=(registers[d]*n)%1000
                ads+=1
                
            case 5:
                registers[d]=registers[n]
                ads+=1
                
            case 6:
                registers[d]=(registers[d]+registers[n])%1000
                ads+=1
                
            case 7:
                registers[d]=(registers[d]*registers[n])%1000
                ads+=1
                
            case 8:
                registers[d]=ram[registers[n]]
                ads+=1
                
            case 9:
                ram[registers[n]]=registers[d]
                ads+=1
        ans+=1

main()
        