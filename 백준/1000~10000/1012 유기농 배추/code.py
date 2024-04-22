import sys
from collections import deque
input = sys.stdin.readline
T = int(input()) #테스트 케이스 입력

def bfs(c,d):
	q = deque([(c,d)]) #큐 초기화
	while q:
		coo = q.popleft()
		x,y=coo[0],coo[1] 
		info = farm[y][x] 
		if info != 0 and info != 2: #해당 지점이 1(배추가 있다면)이라면 
			farm[y][x] = 2 #중복 방지를 위해 2로 변경
			ti = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] #상하좌우로 배추가 있는 부분 탐색을 위한 좌표 저장
			for o,p in ti:
				if o > -1 and o < M and p > -1 and p < N and farm[p][o] == 1: #주어진 농장 범위를 안 벗어나고 1이라면 큐에 추가
					q.append((o,p))
	return #완료되면 근처(붙어 있는)에 있는 배추들은 모두 2로 바뀜 그러면 배추흰지렁이 1개가 필요한 부분..?? 이라고 할수 있다. 

for _ in range(T):
	jiro=0 #지렁이 필요수
	M,N,K=map(int,input().split()) #농장 크기(M,N)와 배추의 개수(K) 입력 받기
	farm = [[0]*M for _ in range(N)] #농장 생성
	for __ in range(K):
		a,b = map(int,input().split()) #배추 심기(?)
		farm[b][a] = 1
	for i in range(M):
		for j in range(N):
			if farm[j][i] == 1: #배추가 있고 탐색이 안된 부분이라면
				bfs(i,j) #bfs수행
				jiro += 1 #bfs수행 끝나면 배추흰지렁이가 1개 필요한거임
	print(jiro)#정답 출력
		
	
