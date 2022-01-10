"""
https://www.acmicpc.net/problem/7682
"""


def check():
    global X_flag, O_flag
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                X_flag += 1
            elif board[0][i] == "O":
                O_flag += 1
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                X_flag += 1
            elif board[i][0] == "O":
                O_flag += 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            X_flag += 1
        elif board[0][0] == "O":
            O_flag += 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            X_flag += 1
        elif board[0][2] == "O":
            O_flag += 1


while True:
    game = input()
    if game[0] == "e":
        break
    board = [
        game[:3],
        game[3:6],
        game[6:]
    ]

    X_cnt = O_cnt = dot_cnt = 0
    X_flag = O_flag = 0
    for i in game:
        if i == "X":
            X_cnt += 1
        elif i == "O":
            O_cnt += 1
        else:
            dot_cnt += 1

    if dot_cnt:  # 승부가 났음
        if X_cnt == O_cnt:  # O가 이겼음
            check()
            if not X_flag and O_flag:
                print("valid")
                continue
        elif X_cnt == O_cnt+1:  # X가 이겼음
            check()
            if X_flag and not O_flag:
                print("valid")
                continue
    else:  # 무승부거나 X가 이겼음
        if X_cnt == 5:
            check()
            if not O_flag:
                print("valid")
                continue

    print("invalid")
