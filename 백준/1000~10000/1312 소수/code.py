A,B,N = input().split()

for i in range(int(N)):
    A = (int(A)%int(B))*10
    j = A//int(B)
print(j)
