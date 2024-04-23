import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
de = deque(list(range(1,N+1))) #기본 순서를 원소로 생각하여 덱 생성
fi = list(map(int,input().split())) #빼내려는 원소의 순서입력 받기
c=0
for i in fi:
	if i == de[0]: #빼내려는 원소가 가장 앞쪽에 있다면 
		de.popleft() #원소를 덱에서 꺼내기
	else:
		while True:
			hf = len(de)//2 #현제 덱의 길이의 절반을 구함
			if de[0] == i: #빼내려는 원소가 가장 앞쪽에 있다면
				de.popleft() #원소를 덱에서 꺼내기
				break
			if de.index(i) <= hf: #빼내야 하는 원소가 절반 앞이라면 
				de.append(de.popleft()) #왼쪽요소들을 오른쪽으로 옮기기 (연산 2)
				c+=1 #한번 할때마다 카운트+1
			else: #빼내야 하는 원소가 절반 뒤라면
				de.appendleft(de.pop()) #오른쪽요소들을 왼쪽으로 옮기기 (연산 3)
				c+=1 #한번 할때마다 카운트+1
		
print(c)
