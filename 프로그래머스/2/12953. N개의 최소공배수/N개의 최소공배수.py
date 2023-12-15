def gcd(a, b):  # 최대공약수
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return -1
def solution(arr):
    answer = 1
    for i in arr:
        answer = answer * i // gcd(answer, i) # 최소공배수 구하기
    return answer