"""
https://www.acmicpc.net/problem/19236
"""
from copy import deepcopy
from sys import stdin
input = stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
A = [[0]*4 for _ in range(4)]
F = [[] for _ in range(17)]
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    A[i][0] = a1
    A[i][1] = a2
    A[i][2] = a3
    A[i][3] = a4
    # 좌표와 방향
    F[a1] = [i, 0, b1-1]
    F[a2] = [i, 1, b2-1]
    F[a3] = [i, 2, b3-1]
    F[a4] = [i, 3, b4-1]


ans = A[0][0]
S = F[A[0][0]][:]
F[A[0][0]] = []
A[0][0] = 0


def move(aqua, fish, shark, cnt): #cnt = 먹은 물고기 수
    global ans
    if ans < cnt:
        ans = cnt

    # 물고기 이동!
    for _fish in fish:
        if not _fish:
            continue
        i, j, d = _fish
        for _ in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (shark[0], shark[1]):
                break
            else:
                d = (d+1)%8
        # ni, nj가 이동할 좌표야!
        now_fish_num = aqua[i][j]
        change_fish_num = aqua[ni][nj]
        aqua[i][j], aqua[ni][nj] = aqua[ni][nj], aqua[i][j]
        # 물고기 정보를 갱신해!
        fish[now_fish_num] = [ni, nj, d]
        # 바뀔 자리에 물고기가 없으면 못바꿔!
        if fish[change_fish_num]:
            fish[change_fish_num][0], fish[change_fish_num][1] = i, j

    si, sj, sd = shark
    while True:
        nsi = si + di[sd]
        nsj = sj + dj[sd]
        si, sj = nsi, nsj
        if not (0 <= nsi < 4 and 0 <= nsj < 4):
            break
        eat = aqua[nsi][nsj]
        if eat == 0:
            continue
        temp_eat = fish[eat][:]
        aqua[nsi][nsj] = 0
        fish[eat] = []
        move(deepcopy(aqua), deepcopy(fish), temp_eat, cnt+eat)
        aqua[nsi][nsj] = eat
        fish[eat] = temp_eat[:]


move(A, F, S, ans)
print(ans)
