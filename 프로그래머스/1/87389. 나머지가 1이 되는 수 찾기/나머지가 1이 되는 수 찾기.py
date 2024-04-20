def solution(n):
    answer = 0
    # n = result * i + 1
    # result = (n-1) // i (11) // 3 => 
    for i in range(1,n):
        if n % i == 1:
            return i