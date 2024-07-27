input=open(0).readline
def main():
	from itertools import permutations
	di={''.join(w):i+1 for i,w in enumerate(permutations("abcdefghi"))}
	for _ in range(int(input())):
		print(di[input().strip()])
main()