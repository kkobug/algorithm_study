"""
https://www.acmicpc.net/problem/23288
"""
# 0부터 동남서북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer_sheet = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if answer_sheet[i][j]:
            continue
        visit = [[False]*M for _ in range(N)]
        visit[i][j] = True
        stack = [(i, j)]
        ans_stack = [(i, j)]
        cnt = 1
        while stack:
            r, c = stack.pop()
            for d in range(4):
                nr = r + di[d]
                nc = c + dj[d]
                if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and board[i][j] == board[nr][nc]:
                    cnt += 1
                    visit[nr][nc] = True
                    stack.append((nr, nc))
                    ans_stack.append((nr, nc))
        while ans_stack:
            r, c = ans_stack.pop()
            answer_sheet[r][c] = board[i][j]*cnt

dice_board = [
    [0, 2, 0],
    [4, 6, 3],
    [0, 5, 0],
]
ans = i = j = d = 0
for _ in range(K):
    # 이 방향 맞아?
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < N and 0 <= nj < M:
        pass
    else:
        d += 2
        d %= 4

    # 돌려!
    num = 7 - dice_board[1][1]
    if d == 0:  # 동쪽
        dice_board[1][0], dice_board[1][1], dice_board[1][2] = dice_board[1][1], dice_board[1][2], num
    elif d == 1:  # 남쪽
        dice_board[0][1], dice_board[1][1], dice_board[2][1] = dice_board[1][1], dice_board[2][1], num
    elif d == 2:  # 서쪽
        dice_board[1][2], dice_board[1][1], dice_board[1][0] = dice_board[1][1], dice_board[1][0], num
    elif d == 3:  # 북쪽
        dice_board[2][1], dice_board[1][1], dice_board[0][1] = dice_board[1][1], dice_board[0][1], num

    i += di[d]
    j += dj[d]
    ans += answer_sheet[i][j]
    if dice_board[1][1] > board[i][j]:
        d += 1
        d %= 4
    elif dice_board[1][1] < board[i][j]:
        d -= 1
        d %= 4

print(ans)