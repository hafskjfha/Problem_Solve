from itertools import permutations 
from bisect import bisect_right
input=open(0).readline
def g():
    k = []
    for tl in range(1, 10):
        for perm in permutations(range(1, 10), tl):
            k.append(int("".join(map(str, perm))))
    return k
def main():
	k = g()
	while 1:
		n=input()
		if n=="":break
		n=int(n)
		if n>=987654321:
			print(0)
			continue
		print(k[bisect_right(k,n)])
main()
