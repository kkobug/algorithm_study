"""
https://www.acmicpc.net/problem/14499
예제 입력 1
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
예제 출력 1
0
0
3
0
0
8
6
3
"""
N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
DB = [
    [0, 2, 0],
    [4, 6, 3],
    [0, 5, 0],
]
dice = [0] * 7

nr, nc = r, c
for k in command:
    if k == 1:
        nc = c + 1
    elif k == 2:
        nc = c - 1
    elif k == 3:
        nr = r - 1
    elif k == 4:
        nr = r + 1

    if not (0 <= nr < N and 0 <= nc < M):
        nr, nc = r, c
        continue
    r, c = nr, nc

    if k == 1:
        DB[1][0] = DB[1][1]
        DB[1][1] = DB[1][2]
        DB[1][2] = 7-DB[1][0]
    elif k == 2:
        DB[1][2] = DB[1][1]
        DB[1][1] = DB[1][0]
        DB[1][0] = 7-DB[1][2]
    elif k == 3:
        DB[2][1] = DB[1][1]
        DB[1][1] = DB[0][1]
        DB[0][1] = 7-DB[2][1]
    elif k == 4:
        DB[0][1] = DB[1][1]
        DB[1][1] = DB[2][1]
        DB[2][1] = 7-DB[0][1]

    if board[r][c] == 0:
        board[r][c] = dice[DB[1][1]]
    else:
        dice[DB[1][1]] = board[r][c]
        board[r][c] = 0
    print(dice[7-DB[1][1]])
