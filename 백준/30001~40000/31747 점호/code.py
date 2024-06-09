#https://github.com/TTC1018/AlgoKotlin/blob/main/src%2Fmain%2Fkotlin%2Fbaekjoon%2Fimplementation%2F31747.kt 을 참고햐여 풀었습니다.
import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split())
A=input().strip().split()
A1,A2,s,t=deque(),deque(),0,0
for i,v in enumerate(A):
	if v=='1':
		A1.append((i,v))
	else:
		A2.append((i,v))

while A1 and A2:
	if A1[0][0]<s+K and A2[0][0]<s+K:
		A1.popleft()
		A2.popleft()
		s+=2
	elif A1[0][0]<s+K:
		A1.popleft()
		s+=1
	else:
		A2.popleft()
		s+=1
	t+=1
print(t+len(A1)+len(A2))
