from collections import deque
def solution(arr):
    answer = deque()
    h = deque(arr)
    while h:
        a = h.popleft()
        if len(h) != 0 and a == h[0]:
            continue
        else:
            answer.append(a)
            
    
    return list(answer)