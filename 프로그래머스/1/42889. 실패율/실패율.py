def solution(N, stages):
    # N+1 사용자, 즉 N번째 클리어한 사용자를 저장하려면 N+2 만큼 필요
    challenger = [0] * (N + 2)
    # 스테이지 별 클리어한 사람들 계산
    for stage in stages:
        challenger[stage] += 1
    # 스테이지 별 실패한 사용자 수 계산
    fails = dict()
    # 각 스테이지 별 인원 수. 초기에는 전체 인원수
    total = len(stages)
    # 각 스테이지 순회하며 실패율 계산
    for i in range(1, N + 1):
        # 도전한 사람이 없는 경우 실패율 0
        if challenger[i] == 0:
            fails[i] = 0
        # 실패율을 구하고 fails 에 저장, 다음 스테이지 인원수 계산
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    # 실패율(value) 에 따라 내림차순 정렬된 실패한 사용자(key) 를 반환
    return sorted(fails, key=lambda x: fails[x], reverse=True)