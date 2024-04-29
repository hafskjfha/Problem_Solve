import sys
input=sys.stdin.readline

memo={}
def w(x,y,z):
	if x<= 0 or y <= 0 or z <= 0:
		return 1
	elif memo.get((x,y,z),False):
		return memo[(x,y,z)]
	elif x > 20 or y > 20 or z > 20:
			memo[(x,y,z)] = w(20,20,20)
			return memo[(x,y,z)]
	elif x < y and y < z:
		memo[(x,y,z)] = w(x,y,z-1) + w(x,y-1,z-1) - w(x,y-1,z)
		return memo[(x,y,z)]
	else:
		memo[(x,y,z)] = w(x-1,y,z) + w(x-1,y-1,z) + w(x-1,y,z-1) - w(x-1,y-1,z-1)
		return memo[(x,y,z)]


while True:
	A,B,C = map(int,input().split())
	if A == -1 and B == -1 and C == -1:
		break
	else:
		print(f"w({A}, {B}, {C}) = {w(A,B,C)}")

