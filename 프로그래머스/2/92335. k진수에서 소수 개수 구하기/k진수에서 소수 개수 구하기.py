import math


def getConvertedNum(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    convertedNumber = getConvertedNum(n, k)
    pList = list(str(convertedNumber).split('0'))
    for eachP in pList:
        if str.isdigit(eachP) and isPrimeNumber(int(eachP)):
            answer += 1
    return answer