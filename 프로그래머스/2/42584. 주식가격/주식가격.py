# 길이를 확정한 주식은 이후 계산에서 제외하기
def solution(prices):
    answer = [0] * len(prices)
    comparePriceIndexStack = [0]
    for i in range(1, len(prices)):
        while comparePriceIndexStack and prices[comparePriceIndexStack[-1]] > prices[i]:
            j = comparePriceIndexStack.pop()
            answer[j] = i - j
        comparePriceIndexStack.append(i)
    while comparePriceIndexStack:
        j = comparePriceIndexStack.pop()
        answer[j] = len(prices) - 1 - j
    return answer