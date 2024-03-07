from collections import deque

def solution(prices):
    answer = []
    priceQueue = deque(prices)

    while priceQueue:
        price = priceQueue.popleft()
        flag = 0
        for p in priceQueue:
            flag += 1
            if price > p:
                break
        answer.append(flag)
    
    return answer