"""
https://www.acmicpc.net/problem/20058
"""
from collections import deque
from copy import deepcopy as dc
from pprint import pprint

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, Q = map(int, input().split())
N = 2**N
ice = [list(map(int, input().split())) for _ in range(N)]
L = list(map(int, input().split()))
temp = dc(ice)

for _k in L:
    # 돌리기
    if _k != 0:
        k = 2 ** _k
        for r in range(0, N, k):
            for c in range(0, N, k):
                for i in range(k):
                    for j in range(k):
                        temp[r+j][c+k-1-i] = ice[r+i][c+j]

    # 얼음 깎기
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0:
                ice[i][j] = 0
                continue
            cnt = 0
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and 0 < temp[ni][nj]:
                    cnt += 1
            if cnt < 3:
                ice[i][j] = temp[i][j] - 1
            else:
                ice[i][j] = temp[i][j]
    temp = dc(ice)


# 남은 얼음
ans = 0
# 가장 큰 덩어리 개수
big_ice = 0
check = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans += ice[i][j]
        if check[i][j]:
            continue
        if ice[i][j] == 0:
            check[i][j] = True
            continue
        Q = deque()
        Q.append((i, j))
        check[i][j] = True
        cnt = 1
        while Q:
            _i, _j = Q.popleft()
            for d in range(4):
                ni = _i + di[d]
                nj = _j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and not check[ni][nj] and 0 < ice[ni][nj]:
                    Q.append((ni, nj))
                    check[ni][nj] = True
                    cnt += 1
        big_ice = max(big_ice, cnt)

print(ans)
print(big_ice)