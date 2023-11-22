# 달력에 대한 값을 잘 세팅할 것,,,,
# for문을 돌 때 몇번째인덱스까지 포함해서 도는 지 유념할 것,,
def solution(a, b):
    cal = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days = 0
    for i in range(0,a-1):
        days += cal[i]
    return date[(days + b) % 7]