def solution(today, terms, privacies):
    answer = []
    termDurationDict = dict()
    for term in terms:
        termName, termMonth = term.split()
        termDurationDict[termName] = int(termMonth) * 28
    privaciesDurations = [0 for _ in range(len(privacies))]
    todayYear, todayMonth, todayDay = today.split(".")
    todayDays = int(todayYear) * 12 * 28 + int(todayMonth) * 28 + int(todayDay)
    print(todayDays)
    # 각 약관에 대해서
    # 약관동의날부터의 파기일을 구하고 -> O(N)
    # 오늘보다 지난 약관들에 대한 index 값을 반환 -> O(N)
    for idx, eachPrivacy in enumerate(privacies):
        privacyDate, privacyName = eachPrivacy.split()
        privacyYear, privacyMonth, privacyDay = privacyDate.split(".")
        deadlineDays = int(privacyYear) * 12 * 28 + int(privacyMonth) * 28 + int(privacyDay)
        privaciesDurations[idx] = termDurationDict[privacyName] + deadlineDays
        print(termDurationDict[privacyName] + deadlineDays)
        if privaciesDurations[idx] <= todayDays:  # 왜,,, 1일이 차이가 나는 거지??
            answer.append(idx + 1)
    return answer