"""
https://www.acmicpc.net/problem/4485
"""
from sys import stdin
import heapq
input = stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
ans = 0
while True:
    N = int(input())
    if not N:
        break
    ans += 1
    cave = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[float('inf')]*N for _ in range(N)]
    cnt[0][0] = cave[0][0]
    heap = [(cave[0][0], 0, 0)]

    while heap:
        now, i, j = heapq.heappop(heap)
        if (i, j) == (N-1, N-1):
            break
        if cnt[i][j] < now:
            continue
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if now + cave[ni][nj] < cnt[ni][nj]:
                    cnt[ni][nj] = now + cave[ni][nj]
                    heapq.heappush(heap, (cnt[ni][nj], ni, nj))
    print(f'Problem {ans}: {cnt[-1][-1]}')