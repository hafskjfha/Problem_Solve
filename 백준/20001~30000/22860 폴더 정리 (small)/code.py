def dfs(folder_map,file_map,query_ans,stackA,v,now):
    if file_map.get(now,[]):
        for fol in stackA:
            query_ans[fol]['unique_files'] |= set(file_map[now])
            query_ans[fol]['all_files'] += len(file_map[now])

    for fol in folder_map.get(now,[]):
        if fol not in v:
            v.add(fol)
            stackA.append(fol)
            dfs(folder_map,file_map,query_ans,stackA,v,fol)
            stackA.pop()
            v.remove(fol)
                

def main():
    import sys
    input=sys.stdin.readline
    print=sys.stdout.write
    file_map={}
    folder_map={}
    fs=set()
    ans=[]

    n,m=map(int,input().split())
    for _ in range(n+m):
        p,f,c=input().split()
        if c=="0":
            file_map.setdefault(p,[]).append(f)
        else:
            folder_map.setdefault(p,[]).append(f)
            fs.add(f)

    query_ans={'main':{'unique_files':set(), 'all_files':0}}
    for fol in fs:
        query_ans[fol] = {'unique_files':set(), 'all_files':0}
    
    dfs(folder_map,file_map,query_ans,['main'],set(['main']),'main')

    for _ in range(int(input())):
        q=input().strip().split('/')
        d=query_ans[q[0]]
        for i in range(1,len(q)):
            d=query_ans[q[i]]
        ans.append(f"{len(d['unique_files'])} {d['all_files']}")
    print('\n'.join(ans))


main()