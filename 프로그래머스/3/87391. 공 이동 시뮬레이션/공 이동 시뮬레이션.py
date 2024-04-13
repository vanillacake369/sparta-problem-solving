def solution(n, m, y, x, queries):
    top = bottom = y  # n행, m열. Parameter x, y 바꿈. 행을 y로 열을 x로 맞추는 것이 익숙해서...
    left = right = x
    for direction, dx in queries[::-1]:
        if direction == 0:  # 열 감소, 거꾸로 생각하면 열 증가
            if left != 0:
                left += dx
                if left > m - 1:
                    left = m - 1
            right += dx
            if right > m - 1:
                right = m - 1
        elif direction == 1:  # 열 증가, 거꾸로 생각하면 열 감소
            left -= dx
            if left < 0:
                left = 0
            if right != m - 1:
                right -= dx
                if right < 0:
                    right = 0
        elif direction == 2:  # 행 감소, 거꾸로 생각하면 행 증가
            if top != 0:
                top += dx
                if top > n - 1:
                    top = n - 1
            bottom += dx
            if bottom > n - 1:
                bottom = n - 1
        elif direction == 3:  # 행 증가, 거꾸로 생각하면 행 감소
            top -= dx
            if top < 0:
                top = 0
            if bottom != n - 1:
                bottom -= dx
                if bottom < 0:
                    top = 0
        if top > n - 1 or bottom < 0 or left > m - 1 or right < 0:
            return 0
    return (bottom - top + 1) * (right - left + 1)