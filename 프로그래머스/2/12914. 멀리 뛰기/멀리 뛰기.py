def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n] % 1234567