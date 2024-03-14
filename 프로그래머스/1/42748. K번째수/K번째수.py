def solution(array, commands):
    answer = []
    for command in commands:
        sortedArr = sorted(array[command[0]-1 : command[1]])
        answer.append(sortedArr[command[2] - 1])
    return answer