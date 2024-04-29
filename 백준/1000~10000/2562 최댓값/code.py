j=[]
for _ in range(9):
    j.append(int(input()))
print(max(j),j.index(max(j))+1,sep="\n")
