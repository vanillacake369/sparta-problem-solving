import heapq

N = int(input())
numbers = []
for _ in range(N):
    eachLineNumbers = map(int, input().split())
    for eachNumber in eachLineNumbers:
        if len(numbers) < N:
            heapq.heappush(numbers, eachNumber)
        else:
            if numbers[0] < eachNumber:
                heapq.heappop(numbers)
                heapq.heappush(numbers, eachNumber)
print(numbers[0])