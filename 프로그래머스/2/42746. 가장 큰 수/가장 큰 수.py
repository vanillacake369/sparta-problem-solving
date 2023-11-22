def solution(numbers):
    # 각 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    # 각 자리수의 숫자 간 비교를 위해 키값을 자리수를 동일하게 만들어줌
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))