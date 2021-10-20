"""
https://www.acmicpc.net/problem/17822
"""
from collections import deque
import sys
input = sys.stdin.readline


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M, T = map(int, input().split())
disk = [[]]
for _ in range(N):
    disk.append(deque(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    t = x
    while t <= N:
        # 회전시키기
        if d:
            disk[t].rotate(-k)
        else:
            disk[t].rotate(k)
        t += x

    adj_list = []
    avg_sum = avg_cnt = 0
    for i in range(1, 1+N):
        for j in range(M):
            if disk[i][j]:
                for d in range(4):
                    ni = i + di[d]
                    nj = (j + dj[d]) % M
                    if 0 < ni <= N and disk[i][j] == disk[ni][nj]:
                        adj_list.append((i, j))
                        break
                else:
                    avg_cnt += 1
                    avg_sum += disk[i][j]
    if adj_list:
        while adj_list:
            i, j = adj_list.pop()
            disk[i][j] = 0
    else:
        if avg_cnt == 0:
            break
        avg = avg_sum/avg_cnt
        for i in range(1, 1+N):
            for j in range(M):
                if disk[i][j]:
                    if disk[i][j] < avg:
                        disk[i][j] += 1
                    elif disk[i][j] > avg:
                        disk[i][j] -= 1
ans = 0
for i in range(1, 1+N):
    for j in range(M):
        if disk[i][j]:
            ans += disk[i][j]
print(ans)
