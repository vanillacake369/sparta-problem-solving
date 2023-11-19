from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    answer = -1 if maps[n-1][m-1] == 1 else  maps[n-1][m-1]
    return answer