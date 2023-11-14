def solution(s, n):
    result = ""
    s = list(s)
    for c in s:
        if c.isupper():
            c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        result += c
    return result
    