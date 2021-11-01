from copy import deepcopy
from sys import stdin
input = stdin.readline


def gravity(x):
    i = j = N - 1
    while 0 <= i:
        if board[i][x] == -2:  # 블록이 없는 자리라면
            pass
        elif board[i][x] == -1:
            while i < j:
                board[j][x] = -2
                j -= 1
            board[j][x] = -1
            j -= 1
        else:
            board[i][x], board[j][x] = board[j][x], board[i][x]
            j -= 1
        i -= 1
    while 0 <= j:
        board[j][x] = -2
        j -= 1


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    # 가장 큰 블록 찾기
    block_ans = []  # 가장 큰 블록
    rainbow_cnt = 0
    visit_total = [[False]*N for _ in range(N)]  # 전체 탐색 현황
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if visit_total[i][j]:  # 이미 그룹검사가 끝난 블록은 탐색 안할거야
                continue
            if board[i][j] < 1:  # 무지개나 검정블록이나 블록이 아닌 자리는 탐색 안할거야
                continue
            visit_now = [[False]*N for _ in range(N)]  # 이번 탐색에 사용될 방문체크
            visit_now[i][j] = True
            visit_total[i][j] = True

            block_temp = [(i, j)]  # 이번 탐색의 결과 블록
            stack = [(i, j)]
            rainbow_temp = 0
            while stack:
                r, c = stack.pop()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and not visit_now[nr][nc]:
                        if board[nr][nc] == 0 or board[nr][nc] == board[i][j]:  # 그룹 체크
                            if board[nr][nc] == 0:
                                rainbow_temp += 1
                            if board[nr][nc] == board[i][j]:  # 같은 블록이면 전체 방문체크 해주기
                                visit_total[nr][nc] = True
                            visit_now[nr][nc] = True
                            block_temp.append((nr, nc))
                            stack.append((nr, nc))

            if 1 < len(block_temp):
                if len(block_ans) < len(block_temp):
                    block_ans = deepcopy(block_temp)
                    rainbow_cnt = rainbow_temp
                elif len(block_ans) == len(block_temp):
                    if rainbow_cnt < rainbow_temp:
                        block_ans = deepcopy(block_temp)
                        rainbow_cnt = rainbow_temp


    if not block_ans:  # 만약 블록 그룹이 존재하지 않으면 그만!
        break

    # 터트리기
    ans += len(block_ans) ** 2
    while block_ans:
        i, j = block_ans.pop()
        board[i][j] = -2
    # 중력
    for k in range(N):
        gravity(k)
    # 반시계 회전
    temp_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_board[N-j-1][i] = board[i][j]
    board = deepcopy(temp_board)
    # 중력
    for k in range(N):
        gravity(k)
print(ans)
