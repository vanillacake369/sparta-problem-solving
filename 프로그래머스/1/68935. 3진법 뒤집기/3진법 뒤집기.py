def getThree(n):
    temp = n
    resultStr = ''
    while temp > 0:
        tempMod = temp % 3
        resultStr += str(tempMod)
        temp //= 3
    return int(resultStr[::-1])


def getTen(reversedThreeN):
    numLen = len(str(reversedThreeN))
    result = 0
    for i in range(0, numLen):
        result += 3 ** (numLen - 1 - i) * int(str(reversedThreeN)[i])
    return result


def solution(n):
    threeN = getThree(n)
    reversedThreeN = int(str(threeN)[::-1])  # reverse string 을 만드는 걸 배웠다 !!
    return getTen(reversedThreeN)