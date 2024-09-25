from collections import deque
def solution(progresses, speeds):
    answer = []
    pr = deque(progresses)
    sp = deque(speeds)
    c=0
    while pr:
        while 1:
            if len(pr) != 0 and pr[0]>=100:
                pr.popleft()
                sp.popleft()
                c += 1
            else:
                if c!=0:
                    answer.append(c)
                    c=0
                break
        for i in range(0,len(pr)):
            pr[i] += sp[i]
    return answer