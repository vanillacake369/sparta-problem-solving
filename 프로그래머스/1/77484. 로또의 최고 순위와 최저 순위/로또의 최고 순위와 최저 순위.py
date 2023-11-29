def solution(lottos, win_nums):
    answer = []
    seq = [6,6,5,4,3,2,1]
    cnt = 0
    zero_cnt = 0
    for l in lottos:
        if(l == 0):
            zero_cnt += 1
    for w in win_nums:
        if(w in lottos):
            cnt += 1
    answer.append(seq[cnt+zero_cnt])
    answer.append(seq[cnt])
    return answer