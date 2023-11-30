# 처음에는 이중for문
# 다음에는 set을 사용
# 마지막으로 0~9까지의 리스트 사용
# 결국 마지막 "000,,"으로 인해 힌트를 참조함
def solution(X, Y):
    answer = ''
    x_lst = [0] * 10
    y_lst = [0] * 10
    for i in range(len(X)) :
        x_lst[int(X[i])] += 1
    for i in range(len(Y)) :
        y_lst[int(Y[i])] += 1
    for i in range(9, -1, -1) :
        for j in range(min(x_lst[i], y_lst[i])) :
            answer += str(i)
    if len(answer) == 0 :
        answer = "-1"
    # "000,,,"인 경우 "0"으로 만들어주기
    elif answer[0] == '0':
        answer = "0"
    return answer