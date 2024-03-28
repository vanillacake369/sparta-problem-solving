def solution(numbers):
    cases = set()
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            cases.add(numbers[i] + numbers[j])

    return sorted(list(cases))