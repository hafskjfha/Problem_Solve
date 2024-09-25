from collections import deque
def solution(s):
    answer = True
    de = deque()
    for c in list(s):
        if c=="(":
            de.append('(')
        elif c==")":
            if len(de) == 0:
                return False
            j = de.pop()
            if j != "(":
                return False
    if de:
        return False
    
    return True