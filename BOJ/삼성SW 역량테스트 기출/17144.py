"""
https://www.acmicpc.net/problem/5373
"""
from copy import deepcopy as dc
from sys import stdin
input = stdin.readline


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, M, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
for i in range(2, N):
    if room[i][0] == -1:
        clean = (i, 0)
        break

temp = dc(room)
for _ in range(T):

    for i in range(N):
        for j in range(M):
            if 4 < room[i][j]:
                A = room[i][j] // 5
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and room[ni][nj] != -1:
                        temp[ni][nj] += A
                        temp[i][j] -= A

    r, c = clean
    for i in range(r-1, 0, -1):
        temp[i][c] = temp[i-1][c]
    for j in range(M-1):
        temp[0][j] = temp[0][j+1]
    for i in range(r):
        temp[i][-1] = temp[i+1][-1]
    for j in range(M-1, 1, -1):
        temp[r][j] = temp[r][j-1]
    temp[r][1] = 0

    r += 1
    for i in range(r+1, N-1):
        temp[i][0] = temp[i+1][0]
    for j in range(M-1):
        temp[-1][j] = temp[-1][j+1]
    for i in range(N-1, r, -1):
        temp[i][-1] = temp[i-1][-1]
    for j in range(M-1, 1, -1):
        temp[r][j] = temp[r][j-1]
    temp[r][1] = 0

    room = dc(temp)

ans = sum(map(sum, room)) + 2
print(ans)