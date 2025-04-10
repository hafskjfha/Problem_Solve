def main():
    n,qq=map(int,input().split())
    logics=input().split('|')
    group_info={}
    group={}
    group_sum={}
    all_group_sum=0
    all_group_count=len(logics)
    j=1
    for i in range(all_group_count):
        for k in logics[i].split('&'):
            k=int(k)
            group.setdefault(i, []).append(k)
            group_sum[i]=group_sum.get(i,0)+k
            group_info[j]=(i,len(group[i])-1)
            j+=1
    s=[]
    
    all_group_sum=sum([group_sum[g]==len(group[g]) for g in group.keys()])
    
    for q in map(int, input().split()):
        group_id, in_group_index = group_info[q]
        old_bit = group[group_id][in_group_index]
        new_bit = 1 ^ old_bit
        was_true = group_sum[group_id] == len(group[group_id])
    
        group[group_id][in_group_index] = new_bit
        group_sum[group_id] += new_bit - old_bit
    
        is_true = group_sum[group_id] == len(group[group_id])
        if was_true != is_true:
            all_group_sum += 1 if is_true else -1
    
        s.append(str(int(all_group_sum != 0)))
    print(''.join(s))
        
main()