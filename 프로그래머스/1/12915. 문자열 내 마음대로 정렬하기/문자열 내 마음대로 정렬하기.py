def solution(strings, n):
    strings.sort() 
    answer = sorted(strings, key=lambda x:x[n])
    return answer

# sorted(strings, key=lambda x:(x[n],x)) 
# =>    lambda에 정렬 우선순위 튜플을 넣을 수 있음
#       이렇게 하면 한 번에 풀림!