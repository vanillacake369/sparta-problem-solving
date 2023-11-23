# 숫자합 조합 중 소수의 개수를 구하기
# 조합 라이브러리가 없으면 직접 구현해야함,,,
import math
import itertools

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    p = []
    cnt = 0
    for i in itertools.combinations(nums,3):
        p.append(sum(i))
    for i in p:
        if isPrime(i):
            cnt += 1
    return cnt