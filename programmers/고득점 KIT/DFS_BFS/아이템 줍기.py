"""
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    cx, cy, ix, iy = map(lambda x: x*2, [characterX, characterY, itemX, itemY])
    answer = 0
    N = 101
    board = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    _di = [1, 1, -1, -1, 0, 1, 0, -1]
    _dj = [1, -1, 1, -1, 1, 0, -1, 0]
    for r in rectangle:
        r = list(map(lambda x: x*2, r))
        for i in range(r[0], r[2]+1):
            for j in range(r[1], r[3]+1):
                board[i][j] = 1

    array = [(rectangle[0][0]*2, rectangle[0][1]*2)]
    remove_list = []
    visit = [[False]*N for _ in range(N)]
    visit[array[0][0]][array[0][1]] = True
    while array:
        i, j = array.pop()
        try:
            for d in range(8):
                ni = i + _di[d]
                nj = j + _dj[d]
                if not board[ni][nj]:
                    break
            else:
                remove_list.append((i, j))
        except:
            pass

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and board[ni][nj]:
                array.append((ni, nj))
                visit[ni][nj] = True

    while remove_list:
        i, j = remove_list.pop()
        board[i][j] = 0

    array = deque()
    array.append((cx, cy))
    visit = [[0]*N for _ in range(N)]
    visit[cx][cy] = 1
    while array and not answer:
        i, j = array.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and board[ni][nj]:
                array.append((ni, nj))
                visit[ni][nj] = visit[i][j] + 1
                if (ni, nj) == (ix, iy):
                    answer = visit[i][j] // 2
                    break
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
print(solution([[2, 2, 49, 49]], 2, 2, 49, 49))
