import heapq


def solution(scoville, K):
    mixCount = 0
    heapq.heapify(scoville)
    while K > scoville[0] :
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        mixed = min1 + (min2 * 2)
        heapq.heappush(scoville, mixed)
        mixCount += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return mixCount