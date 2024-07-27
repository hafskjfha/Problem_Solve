import heapq
input=open(0).readline
sell={}
def main():
	v=0
	for _ in range(int(input())):
		p,name,k,*c=input().strip().split()
		if p=="1":
			if name not in sell:
				sell[name]=[]
			for i in c:
				heapq.heappush(sell.get(name),-int(i))
		elif p=="2":
			try:
				for _ in range(int(k)):
					v+=(-(heapq.heappop(sell[name])))
			except:
				pass
	print(v)
main()