N, M = map(int, input().split())
numbers = list(map(int, input().split()))

i = 0
j = 1
count = 0
while i <= j and j <= N:
    sumFromIToJ = sum(numbers[i:j])
    if sumFromIToJ == M:
        count += 1
        j += 1
    if sumFromIToJ > M:
        i += 1
    if sumFromIToJ < M:
        j += 1
print(count)
