def solution(k, tangerine):
    tangerineSet = dict()
    for t in tangerine:
        tangerineSet[t] = tangerineSet.get(t, 0) + 1
    tangerineDesc = sorted(tangerineSet.items(), key=lambda x: x[1], reverse=True)
    tangerineCount = 0
    for tangerineKeyValue in tangerineDesc:
        k -= tangerineKeyValue[1]
        tangerineCount += 1
        if k <= 0:
            break
    return tangerineCount