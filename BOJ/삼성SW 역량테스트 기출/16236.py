"""
https://www.acmicpc.net/problem/16236
"""
from collections import deque
from sys import stdin
input = stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N = int(input())
room = []
for i in range(N):
    temp = list(map(int, input().split()))
    room.append(temp)
    for j in range(N):
        if temp[j] == 9:
            room[i][j] = 0
            r, c = i, j
size = 2
size_up = 0
ans = 0

while True:
    visit = [[False]*N for _ in range(N)]  # 방문 체크
    Q = deque()                            # 시작점 큐에 담기
    Q.append((r, c))
    visit[r][c] = True                     # 시작점 체크
    dist = 400                             # 먹은순간 간 거리
    eat = []                               # 먹을 수 있는 리스트
    while Q:
        i, j = Q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and visit[i][j] <= dist and room[ni][nj] <= size:  # 안간곳이면
                visit[ni][nj] = visit[i][j] + 1  # 간 거리 체크
                Q.append((ni, nj))
                if 0 < room[ni][nj] < size:  # 먹을 수 있는 물고기는 따로 저장
                    dist = visit[i][j]
                    eat.append((ni, nj))

    if eat:
        nr, nc = N, N
        for _nr, _nc in eat:
            if nr > _nr:
                nr, nc = _nr, _nc
            elif nr == _nr and nc > _nc:
                nc = _nc
        ans += dist
        size_up += 1
        if size_up == size:
            size += 1
            size_up = 0
        room[nr][nc] = 0
        r, c = nr, nc
    else:
        break

print(ans)
