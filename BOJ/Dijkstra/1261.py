"""
https://www.acmicpc.net/problem/1261
"""
from collections import deque

M, N = map(int, input().split())
room = [list(map(int, list(input()))) for _ in range(N)]
cnt = [[10000]*M for _ in range(N)]
cnt[0][0] = 0

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

Q = deque()
Q.append((0, 0))
while Q:
    i, j = Q.popleft()
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if cnt[i][j] + room[ni][nj] < cnt[ni][nj]:
                cnt[ni][nj] = cnt[i][j] + room[ni][nj]
                Q.append((ni, nj))
print(cnt[-1][-1])
