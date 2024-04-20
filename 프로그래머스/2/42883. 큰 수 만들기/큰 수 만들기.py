def solution(number, k):
    answer = ''
    numberList = list(map(int, number))
    numberStack = []

    for idx, eachNumber in enumerate(numberList):
        while k > 0 and len(numberStack) > 0 and numberStack[-1] < eachNumber:
            numberStack.pop()
            k -= 1
        numberStack.append(eachNumber)

    # 반례) 동일한 수가 있는 경우 -> k 가 아직 0이 아니므로 k 만큼 slicing
    if k > 0:
        numberStack = numberStack[:-k]

    return ''.join(list(map(str, numberStack)))