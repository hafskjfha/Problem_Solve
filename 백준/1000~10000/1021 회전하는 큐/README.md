* [문제 링크](https://www.acmicpc.net/problem/1021)

## 문제 정보
<img src="/백준/image/8.svg" width="2%" height="6%" alt="실버3" style="margin-top: 50%;"></img> **회전하는 큐** <br>
| 시간 제한 | 메모리 제한 |
|------|------|
| 2초 | 128MB |

### 문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a<sub>1</sub>, ..., a<sub>k</sub>이었던 것이 a<sub>2</sub>, ..., a<sub>k</sub>와 같이 된다.<br>
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>2</sub>, ..., a<sub>k</sub>, a<sub>1</sub>이 된다.<br>
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>k</sub>, a<sub>1</sub>, ..., a<sub>k-1</sub>이 된다.<br>
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

### 입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
(0≤ M ≤ N ≤ 50)
### 출력
첫째 줄에 문제의 정답을 출력한다.

#### 예제 입력1
<pre>
10 3
1 2 3
</pre>
#### 예제 출력1
<pre>
0
</pre>

#### 예제 입력2
<pre>
10 3
2 9 5
</pre>


#### 예제 출력2
<pre>
8
</pre>

#### 예제 입력3
<pre>
32 6
27 16 30 11 6 23
</pre>

#### 예제 출력3
<pre>
59
</pre>

#### 예제 입력4
<pre>
10 10
1 6 3 2 7 9 8 4 10 5
</pre>

#### 예제 출력4
<pre>
14
</pre>

### 알고리즘 분류
- **자료 구조** <br>
- **덱** <br>

## 문제 풀이


### 정답 코드
[코드](https://github.com/hafskjfha/Problem_Solve/blob/main/%EB%B0%B1%EC%A4%80/1000~10000/1021%20%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94%20%ED%81%90/code.py)
```python
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

```
