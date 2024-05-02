"""
min(scoreBoards) < 입력값:
    heapq.heappop(scoreBoards,
"""
import heapq


def solution(k, score):
    scoreBoards = []
    answer = []
    for idx, s in enumerate(score):
        if len(scoreBoards) < k:
            heapq.heappush(scoreBoards, s)
        elif s > min(scoreBoards):
            heapq.heappop(scoreBoards)
            heapq.heappush(scoreBoards, s)
        answer.append(min(scoreBoards))
    return answer