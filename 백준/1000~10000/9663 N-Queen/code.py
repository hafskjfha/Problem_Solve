def main(N):
    def backtrack(r, cols, diags1, diags2):
        if r == N:
            return 1
        res = 0
        available_positions = (~(cols | diags1 | diags2)) & ((1 << N) - 1)
        while available_positions:
            position = available_positions & -available_positions
            available_positions -= position
            res += backtrack(r + 1, cols | position, (diags1 | position) << 1, (diags2 | position) >> 1)
        return res
    
    return backtrack(0, 0, 0, 0)

print(main(int(input())))
