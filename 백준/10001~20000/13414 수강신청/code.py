import sys
from collections import OrderedDict

def main():
    input = sys.stdin.read
    data = input().split()
    
    to = int(data[0])
    n = int(data[1])
    li = data[2:]
    

    od = OrderedDict()
    for item in reversed(li):
        od[item] = None

    ans = list(od.keys())[::-1]
    
    for i in range(to):
        try:
            print(ans[i])
        except:
            break


main()
