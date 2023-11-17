def solution(s):
    answer = []
    mem = {}
    # mem[a] = 1
    # i = 3
    # s[i] = a
    # diff = 3 - mem[a] = 3-1 = 2
    # answer.append(2)
    # mem[s[i]] = i = mem[a] = 3
    for i in range(0,len(s)):
        if((s[i] in mem) == False):
            answer.append(-1)
            mem[s[i]] = i
        else:
            diff = i - mem[s[i]]
            answer.append(diff)
            mem[s[i]] = i

    return answer