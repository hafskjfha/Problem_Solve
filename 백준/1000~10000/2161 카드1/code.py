from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
card=deque(list(range(1,N+1)))
while len(card) > 1:
	print(card.popleft() ,end=' ')
	card.append(card.popleft())
print(card[0])
