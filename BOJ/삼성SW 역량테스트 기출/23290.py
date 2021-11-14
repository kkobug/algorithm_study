"""
https://www.acmicpc.net/problem/23290
"""
from copy import deepcopy

fi = [0, -1, -1, -1, 0, 1, 1, 1]
fj = [-1, -1, 0, 1, 1, 1, 0, -1]
si = [-1, 0, 1, 0]
sj = [0, -1, 0, 1]

M, S = map(int, input().split())
aquarium = [[[0]*8 for _ in range(4)] for _ in range(4)]

for _ in range(M):
    fx, fy, d = map(int, input().split())
    fx -= 1; fy -= 1; d -= 1
    aquarium[fx][fy][d] += 1

shark = list(map(int, input().split()))
shark[0] -= 1; shark[1] -= 1

smell = [[0]*4 for _ in range(4)]

for _ in range(S):
    # 복제마법 시전!
    temp = deepcopy(aquarium)

    # 물고기 이동!
    aquarium = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for _d in range(8):
                if not temp[i][j][_d]:
                    continue
                d = _d
                for _ in range(8):
                    ni = i + fi[d]
                    nj = j + fj[d]
                    # 범위 안이고, 상어 아니고, 냄새 안나고
                    if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (shark[0], shark[1]) and smell[ni][nj] < 1:
                        aquarium[ni][nj][d] += temp[i][j][_d]
                        break
                    else:
                        d = (d-1) % 8
                else:
                    aquarium[i][j][_d] += temp[i][j][_d]

    cnt = -1
    ans_route = []
    # 상어 이동! 갈 3칸을 고르자
    def move(i, j, idx=0, route=[]):
        global cnt, ans_route
        if idx == 3:
            now_cnt = 0
            # 3칸 속 아쿠아리움을 검사해서, 물고기가 많으면 갱신!
            for ri, rj in set(route):
                for rfish in aquarium[ri][rj]:
                    now_cnt += rfish

            if cnt < now_cnt:
                cnt = now_cnt
                ans_route = deepcopy(route)
            return
        for d in range(4):
            ni = i + si[d]
            nj = j + sj[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                move(ni, nj, idx+1, route+[(ni, nj)])
    move(shark[0], shark[1])

    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    # 경로가 결정되었으니, 그쪽으로 움직이면서 냄새를 남기고 물고기 방빼!
    shark = ans_route[-1][:]
    for ri, rj in set(ans_route):
        is_fish = False
        for rfish in aquarium[ri][rj]:
            if rfish:
                is_fish = True
                break
        if is_fish:
            smell[ri][rj] = 2
            aquarium[ri][rj] = [0] * 8

    # 복제마법 완료!
    for i in range(4):
        for j in range(4):
            for d in range(8):
                aquarium[i][j][d] += temp[i][j][d]

ans = 0
for i in range(4):
    for j in range(4):
        for d in range(8):
            ans += aquarium[i][j][d]

print(ans)
