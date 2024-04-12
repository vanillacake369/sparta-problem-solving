import math


def solution(progresses, speeds):
    answer = []
    leftDaysToFinish = [0] * len(progresses)
    progresseStack = []
    for i in range(len(progresses)):
        leftDaysToFinish[i] = math.ceil((100 - progresses[i]) / speeds[i])
    # 7, 3, 9
    progresseStack.append(leftDaysToFinish[0])  # 7
    count = 1
    for i in range(1, len(leftDaysToFinish) + 1):
        if i == len(leftDaysToFinish):
            answer.append(count)
            break
        if leftDaysToFinish[i] <= progresseStack[-1]:
            count += 1
        else:
            progresseStack.append(leftDaysToFinish[i])
            answer.append(count)
            count = 1
    return answer
