"""
https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""
from collections import deque


def solution(numbers, hand):
    answer = ''
    number_position = [
        (3, 1), (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    left = (3, 0)
    right = (3, 2)

    for number in numbers:
        if number in (1, 4, 7):
            left = number_position[number]
            answer += "L"
        elif number in (3, 6, 9):
            right = number_position[number]
            answer += "R"
        else:
            dist_board = [[-1] * 3 for _ in range(4)]
            i, j = number_position[number]
            dist_board[i][j] = 0
            Q = deque()
            Q.append((i, j))
            while Q:
                i, j = Q.popleft()
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < 4 and 0 <= nj < 3 and dist_board[ni][nj] == -1:
                        dist_board[ni][nj] = dist_board[i][j] + 1
                        Q.append((ni, nj))

            left_value = dist_board[left[0]][left[1]]
            right_value = dist_board[right[0]][right[1]]
            if left_value == right_value:
                if hand == "right":
                    right = number_position[number]
                    answer += "R"
                else:
                    left = number_position[number]
                    answer += "L"
            elif left_value < right_value:
                left = number_position[number]
                answer += "L"
            else:
                right = number_position[number]
                answer += "R"
    return answer


print(solution(
    [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
))
print(solution(
    [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
))
print(solution(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
))
