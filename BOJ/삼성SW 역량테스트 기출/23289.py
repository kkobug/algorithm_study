"""
https://www.acmicpc.net/problem/23289
"""
from copy import deepcopy
from collections import deque


def heat(i, j, d):
    i += di[d]
    j += dj[d]
    stack = deque([(i, j, 5)])
    ret = [[0]*C for _ in range(R)]
    visit = [[False]*C for _ in range(R)]
    while stack:
        _i, _j, now = stack.popleft()
        ret[_i][_j] = now
        # 다음 방향으로 갈 수 있어?
        if not wall[_i][_j][d]:
            ni = _i + di[d]
            nj = _j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and 1 < now and not visit[ni][nj]:
                stack.append((ni, nj, now-1))
                visit[ni][nj] = True
        if d in (0, 1):
            nd = (2, 3)
        else:
            nd = (0, 1)

        for _d in nd:
            if wall[_i][_j][_d]:
                continue
            ni = _i + di[_d]
            nj = _j + dj[_d]
            if not (0 <= ni < R and 0 <= nj < C):
                continue
            if wall[ni][nj][d]:
                continue
            ni += di[d]
            nj += dj[d]
            if 0 <= ni < R and 0 <= nj < C and 1 < now and not visit[ni][nj]:
                stack.append((ni, nj, now-1))
                visit[ni][nj] = True
    return ret


ans = 0
R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
heater = []  # 온풍기 좌표, 방향
check_point = []  # 여기를 검사해!
for i in range(R):
    for j in range(C):
        if not room[i][j]:
            continue
        if room[i][j] == 5:
            check_point.append((i, j))
        elif room[i][j]:
            heater.append((i, j, room[i][j]-1))
        room[i][j] = 0

wall = [[[False]*4 for _ in range(C)] for _ in range(R)]
W = int(input())
# 0 : 오른쪽, 1 : 왼쪽, 2 : 위, 3 : 아래
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1; y -= 1;
    if t:  # x, y에서 오른쪽 가는거랑 x, y+1에서 왼쪽 가는길 벽
        wall[x][y][0] = wall[x][y+1][1] = True
    else:
        wall[x][y][2] = wall[x-1][y][3] = True

while ans <= 100:
    # heater
    for i, j, d in heater:
        now_heat = heat(i, j, d)
        for r in range(R):
            for c in range(C):
                if now_heat[r][c]:
                    room[r][c] += now_heat[r][c]
    # heat transfer
    temp_room = deepcopy(room)
    for i in range(R):
        for j in range(C):
            if room[i][j] < 4:
                continue
            now = room[i][j]
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < R and 0 <= nj < C:
                    if room[i][j] <= room[ni][nj] or wall[i][j][d]:
                        continue
                    diff = (room[i][j] - room[ni][nj]) // 4
                    temp_room[ni][nj] += diff
                    temp_room[i][j] -= diff
    room = deepcopy(temp_room)

    # decrease T
    for i in range(R):
        if room[i][0]:
            room[i][0] -= 1
        if room[i][-1]:
            room[i][-1] -= 1
    for j in range(1, C-1):
        if room[0][j]:
            room[0][j] -= 1
        if room[-1][j]:
            room[-1][j] -= 1

    # eat chocolate
    ans += 1

    # is ans?
    flag = True
    for i, j in check_point:
        if room[i][j] < K:
            flag = False
            break
    if flag:
        break
print(ans)