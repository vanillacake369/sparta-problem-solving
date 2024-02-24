import math

def solution(progresses, speeds):
    answer = []

    # 1
    # for 문을 사용하여 구한 필요한작업기간리스트
    # leftProgresses = []
    # for idx,p in progresses:
    #     leftProgresses.append((100 - p) // speeds[idx])
    # list comprehension 을 사용하여 구한 필요한작업기간리스트
    leftProgresses = [math.ceil((100 - p) / speeds[idx]) for idx, p in enumerate(progresses)]

    # 2
    leftPStack = [leftProgresses[0]]
    daysToDeploy = 0
    for pr in leftProgresses:
        if(pr <= leftPStack[-1]):
            daysToDeploy += 1
        else:
            answer.append(daysToDeploy)
            leftPStack.append(pr)
            daysToDeploy = 1
    answer.append(daysToDeploy)
    return answer