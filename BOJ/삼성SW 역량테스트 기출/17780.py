"""
https://www.acmicpc.net/problem/17780
"""
from sys import stdin
input = stdin.readline

def move():
    over = game[i][j][idx:]  # 움직이는 말 위의 stack 다 모으기
    if board[ni][nj]:
        over = over[::-1]  # 다음칸이 빨강이면 뒤집기
    game[i][j] = game[i][j][:idx]  # 지금 칸은 움직이는말 아래만 남기고 지우기
    game[ni][nj] += over  # 다음 칸에 얹기
    for m in over:  # 좌표 갱신
        player[m][0] = ni
        player[m][1] = nj


di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 색깔 확인
player = []  # 플레이어 현황 (플레이어 좌표, 방향)
game = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(K):
    i, j, d = map(int, input().split())
    player.append([i-1, j-1, d-1])
    game[i-1][j-1].append(_)

flag = True  # 4칸이 넘지 않는다면 True
ans = 0
while flag and ans < 1000:
    ans += 1
    for turn in range(K):
        i, j, d = player[turn]
        idx = game[i][j].index(turn)
        if idx:  # idx가 0이 아닐 경우, 가장 아래 말이 아니므로 continue
            continue
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 2:  # 다음 칸이 흰색/빨간색이라면
            move()
            if 4 <= len(game[ni][nj]):
                flag = False
                break
        else:
            # 다음 칸이 파랑이거나 없으면
            if d == 2:
                d = 3
            elif d == 3:
                d = 2
            else:
                d = 1 - d
            player[turn][2] = d  # 뒤돌아서 다시 다음칸 검사
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 2:
                move()
                if 4 <= len(game[ni][nj]):
                    flag = False
                    break
if flag:
    print(-1)
else:
    print(ans)
