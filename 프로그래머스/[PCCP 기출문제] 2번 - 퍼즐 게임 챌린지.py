def puzzle_solve(di,ti,li,le):
    all_time=0
    time_prev=0
    
    for i in range(len(di)):
        if di[i]-le>0:
            all_time+=(time_prev+ti[i])*(di[i]-le)
        all_time+=ti[i]
        time_prev=ti[i]
    return 0 if all_time>li else 1

def solution(diffs, times, limit):
    answer = 0
    start,end=1,100000
    while start<=end:
        mid=(start+end)//2
        if puzzle_solve(diffs,times,limit,mid):
            end=mid-1
            answer=mid
        else:
            start=mid+1
    return answer
