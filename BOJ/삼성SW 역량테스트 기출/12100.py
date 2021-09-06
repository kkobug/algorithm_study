"""
https://www.acmicpc.net/problem/12100
보드를 돌릴까?
상하좌우를 다 구현할까?
"""
from sys import stdin as st
from copy import deepcopy as dc

def push(d):
    if d == 0:  # 위로 밀기
        for j in range(N):
            top = 0
            for i in range(1, N):
                if board[i][j]:
                    if not board[top][j]:
                        board[top][j] = board[i][j]
                        board[i][j] = 0
                    elif board[top][j] == board[i][j]:
                        board[top][j] *= 2
                        board[i][j] = 0
                        top += 1
                    else:
                        top += 1
                        board[top][j] = board[i][j]
                        if top != i: board[i][j] = 0

    elif d == 1:  # 오른쪽으로 밀기
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    if not board[i][top]:
                        board[i][top] = board[i][j]
                        board[i][j] = 0
                    elif board[i][top] == board[i][j]:
                        board[i][top] *= 2
                        board[i][j] = 0
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = board[i][j]
                        if top != j: board[i][j] = 0


    elif d == 2:  # 아래로 밀기
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    if not board[top][j]:
                        board[top][j] = board[i][j]
                        board[i][j] = 0
                    elif board[top][j] == board[i][j]:
                        board[top][j] *= 2
                        board[i][j] = 0
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = board[i][j]
                        if top != i: board[i][j] = 0

    else:  # 왼쪽으로 밀기
        for i in range(N):
            top = 0
            for j in range(1, N):
                if board[i][j]:
                    if not board[i][top]:
                        board[i][top] = board[i][j]
                        board[i][j] = 0
                    elif board[i][top] == board[i][j]:
                        board[i][top] *= 2
                        board[i][j] = 0
                        top += 1
                    else:
                        top += 1
                        board[i][top] = board[i][j]
                        if top != j: board[i][j] = 0


def game(tc=0):
    global ans, board
    if tc == 5:
        for m in range(N):
            max_val = max(board[m])
            if ans < max_val:
                ans = max_val
        return
    
    temp = dc(board)  # 복구용
    for i in range(4):
        push(i)
        game(tc+1)
        board = dc(temp)
        

N = int(st.readline())
board = [list(map(int, st.readline().split())) for _ in range(N)]
ans = 0
game()
print(ans)
