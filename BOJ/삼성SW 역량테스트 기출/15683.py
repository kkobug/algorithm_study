"""
https://www.acmicpc.net/problem/15683
"""
from copy import deepcopy as dc


def watch(x, y, dx, dy, X):  # 감시하는 함수
    x += dx
    y += dy
    while 0 <= x < N and 0 <= y < M and X[x][y] != 6:
        if X[x][y] == 0:
            X[x][y] = 9
        x += dx
        y += dy


def case(OFF, idx=0):
    global ans
    if ans == 0:
        return

    if idx == len(CCTV):
        zero_cnt = 0
        for n in OFF:
            zero_cnt += n.count(0)
        ans = min(ans, zero_cnt)
        return

    temp = dc(OFF)
    i, j = CCTV[idx]
    if OFF[i][j] == 1:
        for d in range(4):
            watch(i, j, di[d], dj[d], OFF)
            case(OFF, idx + 1)
            OFF = dc(temp)

    elif OFF[i][j] == 2:
        for d in range(2):
            watch(i, j, di[d], dj[d], OFF)
            watch(i, j, di[d + 2], dj[d + 2], OFF)
            case(OFF, idx + 1)
            OFF = dc(temp)

    elif OFF[i][j] == 3:
        for d in range(4):
            watch(i, j, di[d], dj[d], OFF)
            watch(i, j, di[(d + 1) % 4], dj[(d + 1) % 4], OFF)
            case(OFF, idx + 1)
            OFF = dc(temp)

    elif OFF[i][j] == 4:
        for d in range(4):
            watch(i, j, di[d], dj[d], OFF)
            watch(i, j, di[(d + 1) % 4], dj[(d + 1) % 4], OFF)
            watch(i, j, di[(d + 2) % 4], dj[(d + 2) % 4], OFF)
            case(OFF, idx + 1)
            OFF = dc(temp)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
office = []
CCTV = []
five = []
for i in range(N):
    temp = list(map(int, input().split()))
    office.append(temp)
    for j in range(M):
        if 0 < temp[j] < 5:
            CCTV.append((i, j))
        elif temp[j] == 5:
            five.append((i, j))

for F in five:  # 5번 카메라는 경우를 따질 필요가 없다
    i, j = F
    for d in range(4):
        watch(i, j, di[d], dj[d], office)

ans = 65
case(office)
print(ans)
