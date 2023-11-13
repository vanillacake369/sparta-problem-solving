# 모든 경우의 수를 체크해야함 
# :: 학생이 정렬되어있지 않은 입력, 각 입력의 공통요소,빌려주고 나서의 처리
# 내 손으로 풀지 못 했음,,,
def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)