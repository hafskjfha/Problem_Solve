import string
S=input()
ls = list(string.ascii_lowercase)
p={}
for i in ls:
	p[i]=-1
for j in set(S):
	if p[j]==-1:
		p[j]=S.index(j)
for c in p.values():
	print(c,end=" ")
