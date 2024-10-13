def sort(lst):
    mid=len(lst)//2
    left, right = lst[:mid], lst[mid:]
    lst[:] = []
    l_len, r_len = len(left), len(right)
    if l_len > 1: sort(left)
    if r_len > 1: sort(right)

    l, r = 0, 0
    while (l < l_len) & (r < r_len):
        if int(str(left[l])+str(right[r])) >= int(str(right[r])+str(left[l])):
            lst.append(left[l])
            l += 1
        else:
            lst.append(right[r])
            r += 1
    lst.extend(left[l:])
    lst.extend(right[r:])
    return lst
input()
print(int("".join(map(str,sort([*map(int,input().split())])))))
