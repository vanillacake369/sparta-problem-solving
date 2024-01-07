def dfs(result,input_list,pick,level,dynamic_pick_count):
		# pick_count 모두 뽑았으면 출력하고 리턴
    if level == dynamic_pick_count:
        result.append(''.join(pick))
        return
    for i in range(len(input_list)):
        pick[level] = input_list[i]  # 카드 뽑고
        dfs(result,input_list,pick,level+1,dynamic_pick_count)  # 다음 카드 뽑으러 가기
        pick[level] = 0  # 리턴 이후 뽑은 카드 초기화

def solution(word):
    answer = 0
    pick_count = 5
    input_list = [ 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(1,pick_count+1):
        pick = [0] * i
        dfs(result,input_list,pick,0,i)
    result.sort()
    answer = result.index(word) + 1
    return answer