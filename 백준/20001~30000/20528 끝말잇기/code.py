def main():
	k=""
	n=input()
	for S in input().split():
		if not k:
			k=S[0]
		if S[0]!=k and S[-1]!=k:
			print(0)
			break
	else:
		print(1)
	
	
main()
