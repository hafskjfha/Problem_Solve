def main():
    encode=str.encode
    import os
    P=os.read(0,os.stat(0).st_size).decode().split('\n')
    N = int(P[0]) 
    A = sorted(map(int, P[1].split())) 
    i, j = 0, N - 1
    mini, minj = 0, N - 1
    mina = float('inf')
    
    while i < j:
        if A[i] + A[j] < 0:
            if abs(A[i] + A[j]) < abs(mina):
                mini, minj = i, j
                mina = A[i] + A[j]
            i += 1
        elif A[i] + A[j] > 0:
            if abs(A[i] + A[j]) < abs(mina):
                mini, minj = i, j
                mina = A[i] + A[j]
            j -= 1
        else:
            mini, minj = i, j
            mina = A[i] + A[j]
            break
    
    os.write(1, encode(f'{A[mini]} {A[minj]}'))

    
    os._exit(os.EX_OK)

main()
