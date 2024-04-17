n, r, c = map(int, input().split())

def recursive(n, row, col):
    if n == 0:
        return 0
    curRow = row % 2
    curCol = col % 2
    rcPlus = 2 * curRow + curCol
    return 4 * recursive(n - 1, row // 2, col // 2) + rcPlus


print(recursive(n, r, c))
