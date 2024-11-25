l=[input()for _ in range(5)]
for i in range(len(max(l,key=lambda x:len(x)))):
    for j in range(5):
        try:
            print(l[j][i],end="")
        except:
            pass
