def isLeftSide(choice):
    if choice < 4:
        return True
    return False


def getResultStrOf(dict):
    dictValues = list(dict.values())
    if dictValues[0] == dictValues[1]:
        alphaBetAsc = list(sorted(dict.items(), key=lambda x: x[0]))
        return alphaBetAsc[0][0]
    else:
        scoreDesc = list(sorted(dict.items(), key=lambda x: x[1], reverse=True))
        return scoreDesc[0][0]


def solution(survey, choices):
    answer = ''
    # R,T/F,C/M,J,/A,N
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    dictAN = {'A': 0, 'N': 0}
    dictRT = {'R': 0, 'T': 0}
    dictCF = {'C': 0, 'F': 0}
    dictMJ = {'M': 0, 'J': 0}
    for idx, choice in enumerate(choices):
        choiceScore = score[choice]
        firstLetterOfEachSurvey = survey[idx][0]
        secondLetterOfEachSurvey = survey[idx][1]
        if firstLetterOfEachSurvey == 'A' or firstLetterOfEachSurvey == 'N':
            if isLeftSide(choice):
                dictAN[firstLetterOfEachSurvey] += choiceScore
            else:
                dictAN[secondLetterOfEachSurvey] += choiceScore
        if firstLetterOfEachSurvey == 'R' or firstLetterOfEachSurvey == 'T':
            if isLeftSide(choice):
                dictRT[firstLetterOfEachSurvey] += choiceScore
            else:
                dictRT[secondLetterOfEachSurvey] += choiceScore
        if firstLetterOfEachSurvey == 'C' or firstLetterOfEachSurvey == 'F':
            if isLeftSide(choice):
                dictCF[firstLetterOfEachSurvey] += choiceScore
            else:
                dictCF[secondLetterOfEachSurvey] += choiceScore
        if firstLetterOfEachSurvey == 'M' or firstLetterOfEachSurvey == 'J':
            if isLeftSide(choice):
                dictMJ[firstLetterOfEachSurvey] += choiceScore
            else:
                dictMJ[secondLetterOfEachSurvey] += choiceScore
    answer = getResultStrOf(dictRT) + getResultStrOf(dictCF) + getResultStrOf(dictMJ) + getResultStrOf(dictAN)
    return answer