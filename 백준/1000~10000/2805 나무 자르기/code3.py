import bisect
input = open(0).readline
sA = []

def sol(K, A, M):
    global sA
    p = bisect.bisect_left(A, K)
    s = (sA[-1] - sA[p]) - K * (len(A) - p)
    return 0 if s < M else 1

def main():
    global sA
    N, M = map(int, input().split())
    A = sorted([*map(int, input().split())])
    sA = [0] * (N + 1)
    for i in range(1, N + 1):
        sA[i] = sA[i - 1] + A[i - 1]
    
    start, end = 0, A[-1]
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if sol(mid, A, M):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(ans)

main()
