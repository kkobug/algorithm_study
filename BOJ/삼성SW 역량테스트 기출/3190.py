# https://www.acmicpc.net/problem/3190
from sys import stdin as st

di = [0, 1, 0, -1]  # 방향이 L이면 d-1, D면 d+1
dj = [1, 0, -1, 0]

N = int(st.readline())  # 보드의 크기
board = [[True]*(N+1) for _ in range(N+1)]  # 보드
board[1][1] = False  # 시작점

K = int(st.readline())  # 사과 놓기
for apple in range(K):
    i, j = map(int, st.readline().split())
    board[i][j] = 2

L = int(st.readline())  # 방향 변환 횟수
turn = [list(input().split()) for _ in range(L)]

# 머리 정보
i = j = 1
d = cnt = idx = 0
# 꼬리 정보
tail_i = tail_j = 1
tail_d = tail_cnt = tail_idx = 0

while True:
    i += di[d]
    j += dj[d]
    cnt += 1
    if not (0 < i <= N and 0 < j <= N and board[i][j]):
        break

    if cnt == int(turn[idx][0]):
        if turn[idx][1] == 'D':
            d = (d+1)%4
        else:
            d = (d-1)%4
        idx = (idx+1)%L

    if board[i][j] != 2:
        board[tail_i][tail_j] = True
        tail_i += di[tail_d]
        tail_j += dj[tail_d]
        tail_cnt += 1

        if tail_cnt == int(turn[tail_idx][0]):
            if turn[tail_idx][1] == 'D':
                tail_d = (tail_d + 1) % 4
            else:
                tail_d = (tail_d - 1) % 4
            tail_idx = (tail_idx+1)%L
    board[i][j] = False

print(cnt)
