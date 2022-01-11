"""
https://www.acmicpc.net/problem/11658
"""
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ref = [[] for _ in range(N)]
for i in range(N):
    value = 0
    for j in range(N):
        value += arr[i][j]
        ref[i].append(value)

for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0]:
        ans = 0
        if 0 <= cmd[2]-2:
            for i in range(cmd[1]-1, cmd[3]):
                ans += ref[i][cmd[4]-1] - ref[i][cmd[2]-2]
        else:
            for i in range(cmd[1]-1, cmd[3]):
                ans += ref[i][cmd[4]-1]
        print(ans)
    else:
        x, y = cmd[1]-1, cmd[2]-1
        delta = cmd[3] - arr[x][y]
        arr[x][y] = cmd[3]
        for j in range(y, N):
            ref[x][j] += delta
