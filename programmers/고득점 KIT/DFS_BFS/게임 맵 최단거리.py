"""
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    check = [[-1] * m for _ in range(n)]
    check[0][0] = 1
    Q = deque()
    Q.append((0, 0))

    while Q:
        i, j = Q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] and check[ni][nj] == -1:
                check[ni][nj] = check[i][j] + 1
                Q.append((ni, nj))

    return check[n-1][m-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
