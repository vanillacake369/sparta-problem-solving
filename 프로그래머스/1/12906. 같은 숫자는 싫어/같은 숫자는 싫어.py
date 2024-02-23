def solution(arr):
    answer = []
    previous = -1
    for num in arr:
        if num in answer:
            if previous != num:
                answer.append(num)
                previous = num
            else:
                continue
        else:
            previous = num
            answer.append(num)
    return answer