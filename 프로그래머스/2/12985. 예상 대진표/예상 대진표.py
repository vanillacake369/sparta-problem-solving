def solution(n,a,b):
    answer = 0
    ra = a
    rb = b
    while(True):
        ra = ra // 2 + ra % 2
        rb = rb // 2 + rb % 2
        answer += 1
        if(ra == rb):
            break
    return answer