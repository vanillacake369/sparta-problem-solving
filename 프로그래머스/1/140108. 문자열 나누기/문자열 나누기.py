# 문제를 잘 읽어야 했던 문제,,,
# 상상의 나래를 펼치지 않았으면,,, 부디,,, 제봘,,,
def solution(s):
    answer = 0
    i = 0
    while i < len(s) :
        n = 1
        m = 0
        j = 1
        while n != m and i + j < len(s) :
            if s[i] == s[i + j] :
                n += 1
            else :
                m += 1
            j += 1
        answer += 1
        i += j
    return answer