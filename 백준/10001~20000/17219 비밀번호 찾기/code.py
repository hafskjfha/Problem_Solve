import sys
input=sys.stdin.readline
N,M=map(int,input().split())
pas={}
for _ in range(N):
	ifom = input().strip().split()
  pas[ifom[0]]=ifom[1]
for _ in range(M):
	site=input().strip()
	print(pas[site])
