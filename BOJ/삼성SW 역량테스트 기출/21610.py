"""
https://www.acmicpc.net/problem/21610
"""
from copy import deepcopy as dc
from sys import stdin
input = stdin.readline

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
cloud = [[False]*N for _ in range(N)]
# 비바리기 시전
cloud[N-1][0] = cloud[N-1][1] = cloud[N-2][0] = cloud[N-2][1] = True

for _ in range(M):
    d, s = map(int, input().split())

    # 1. 모든 구름이 이동한다
    temp_cloud = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ni = (i + s*di[d]) % N
            nj = (j + s*dj[d]) % N
            temp_cloud[ni][nj] = cloud[i][j]
    cloud = dc(temp_cloud)

    # 2. 구름에서 비가 내려 바구니 물의 양 +1
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                basket[i][j] += 1

    # 3. 구름이 모두 사라진다

    # 4. 2에서 물이 증가한 칸 대각선을 검사한다.
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:  # 2에서 물이 증가한 칸에 한해서 마법을 시전
                for nd in [2, 4, 6, 8]:
                    ni = i + di[nd]
                    nj = j + dj[nd]
                    if 0 <= ni < N and 0 <= nj < N and basket[ni][nj]:
                        basket[i][j] += 1

    # 5. 바구니에 저장된 양이 2 이상인 칸에는 다시 구름이 생긴다.
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                cloud[i][j] = False
            else:
                if 2 <= basket[i][j]:
                    cloud[i][j] = True
                    basket[i][j] -= 2

print(sum(map(sum, basket)))