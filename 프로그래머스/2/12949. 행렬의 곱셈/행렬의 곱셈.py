def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])

    for i in range(m):
        arr = arr1[i]
        result = []
        for j in range(r):
            hap = 0
            for k in range(n):
                hap += arr[k] * arr2[k][j]
            result.append(hap)
        answer.append(result)

    return answer

# Ver1
# def solution(arr1, arr2):
#     m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
#     answer = [[0 for _ in range(r)] for _ in range(m)] # m * r 크기의 행렬
#     for i in range(m):
#         for k in range(r):
#             for j in range(n):
#                 answer[i][k] += arr1[i][j] * arr2[j][k]
#     return answer

# Ver2
# def solution(arr1, arr2):
#     return [[sum(i*j for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1