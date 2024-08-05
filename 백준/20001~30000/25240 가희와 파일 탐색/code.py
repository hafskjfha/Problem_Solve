input=open(0).readline
U,F=map(int,input().split())
user={}
file={}
power=['','X','WR','WRX','R','RX','WR','WRX']
def access(user_name,file_name,work):
    file_owrer=file[file_name]['owrer'][0]
    if file_owrer==user_name:
        return 1 if work in file[file_name]['owrer'][1]else 0
    elif file[file_name]['group'][0] in user[user_name]:
        file_group=file[file_name]['group'][0]
        return 1 if work in file[file_name]['group'][1]else 0
    else:
        return 1 if work in file[file_name]['other']else 0

def main():
    for _ in range(U):
        name,*k=input().strip().split()
        if k:
            k=k[0].split(',')
            user[name]=set(k)|set([name])
        else:
            user[name]=set([name])
    for _ in range(F):
        f_NAME,f_PERMISSION,f_OWNER,f_OWNED_GROUP=input().strip().split()
        file[f_NAME]={'owrer':[f_OWNER,power[int(f_PERMISSION[0])]],
                      'group':[f_OWNED_GROUP,power[int(f_PERMISSION[1])]],
                      'other':power[int(f_PERMISSION[2])]
        }
    for _ in range(int(input())):
        un,fn,op=input().strip().split()
        print(access(un,fn,op))
main()
