def solution(participant, completion):
    hashP = dict()
    sum = 0

    for p in participant:
        hashP[hash(p)] = p
        sum += hash(p)

    for c in completion:
        sum -= hash(c)

    return hashP[sum]