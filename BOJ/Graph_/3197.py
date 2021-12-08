"""
https://www.acmicpc.net/problem/3197
"""
from collections import deque
from sys import stdin
input = stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

R, C = map(int, input().split())
lake = []
swan = []
for i in range(R):
    _ = list(input())
    lake.append(_)
    for j in range(C):
        if _[j] == "L":
            swan.append((i, j))
            lake[i][j] = "."

met = False
ans = 0
# 녹이기 위한 체크리스트 & 좌표 큐
visit = [[False] * C for _ in range(R)]
melt_Q = deque()
# 백조가 이동하기 위한 체크리스트 & 좌표 큐
swan_visit = [[False] * C for _ in range(R)]
swan_Q = deque()
# 백조가 있는 위치 체크
visit[swan[0][0]][swan[0][1]] = swan_visit[swan[0][0]][swan[0][1]] = True

# 녹은 후 백조가 이동할 수 있는 위치를 swan_Q에 담기 + 녹을 위치 담기
Q = deque([(swan[0][0], swan[0][1])])
while Q:
    i, j = Q.popleft()
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < R and 0 <= nj < C and not visit[ni][nj]:
            visit[ni][nj] = True
            swan_visit[ni][nj] = True
            if lake[ni][nj] == ".":
                Q.append((ni, nj))
            else:
                melt_Q.append((ni, nj))
                swan_Q.append((ni, nj))

# 백조가 없는 영역에서 녹을 위치도 담기 위해 반복 돌면서 BFS
for i in range(R):
    for j in range(C):
        if lake[i][j] == "X" or visit[i][j]:
            continue
        Q = deque([(i, j)])
        while Q:
            r, c = Q.popleft()
            for d in range(4):
                ni = r + di[d]
                nj = c + dj[d]
                if 0 <= ni < R and 0 <= nj < C and not visit[ni][nj]:
                    visit[ni][nj] = True
                    if lake[ni][nj] == ".":
                        Q.append((ni, nj))
                    else:
                        melt_Q.append((ni, nj))

while not met:
    next_swan_Q = deque()
    next_melt_Q = deque()
    # 일단 녹이기
    while melt_Q:
        i, j = melt_Q.popleft()
        lake[i][j] = "."
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and not visit[ni][nj]:
                if lake[ni][nj] == "X":
                    visit[ni][nj] = True
                    next_melt_Q.append((ni, nj))

    # 백조가 이동할 수 있는 영역 다시 확인하기
    while swan_Q:
        i, j = swan_Q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and not swan_visit[ni][nj]:
                swan_visit[ni][nj] = True
                if lake[ni][nj] == ".":
                    swan_Q.append((ni, nj))
                    if (ni, nj) == swan[1]:
                        met = True
                else:
                    next_swan_Q.append((ni, nj))

    melt_Q = next_melt_Q
    swan_Q = next_swan_Q
    ans += 1

print(ans)
