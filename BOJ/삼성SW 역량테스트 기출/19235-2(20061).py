"""
https://www.acmicpc.net/problem/20061
"""
from collections import deque
from sys import stdin
input = stdin.readline

def down(board, block, ver, hor):
    stack = [(0, block)]
    while stack:
        i, j = stack.pop()
        ni = i + 1
        if 0 <= ni < 6 and not board[ni][j]:
            i = ni
            stack.append((ni, j))
    if hor:
        stack = [(0, block+1)]
        while stack:
            vi, _j = stack.pop()
            ni = vi + 1
            if 0 <= ni < 6 and not board[ni][_j]:
                vi = ni
                stack.append((ni, _j))
        i = min(i, vi)
        board[i][j+1] = True
    if ver:
        board[i-1][j] = True
    board[i][j] = True


def bomb(board):
    global ans
    k = 5
    while 1 < k:
        if sum(board[k]) == 4:
            del board[k]
            board.appendleft([False] * 4)
            ans += 1
        else:
            k -= 1
    while 0 <= k:
        if sum(board[k]):
            board.pop()
            board.appendleft([False] * 4)
        else:
            k -= 1


green = deque([False]*4 for _ in range(6))
blue = deque([False]*4 for _ in range(6))
ans = 0
for _ in range(int(input())):
    t, i, j = map(int, input().split())
    hor_green = hor_blue = ver_green = ver_blue = False
    green_block = j
    blue_block = 3-i
    if t == 2:
        hor_green = True
        ver_blue = True
    elif t == 3:
        ver_green = True
        hor_blue = True
        blue_block = 2-i

    # 타일 내리기
    down(green, green_block, ver_green, hor_green)
    down(blue, blue_block, ver_blue, hor_blue)

    # 타일 삭제
    bomb(green)
    bomb(blue)
print(ans)
print(sum(map(sum, green)) + sum(map(sum, blue)))
