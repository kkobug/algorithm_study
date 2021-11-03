"""
https://www.acmicpc.net/problem/2665
"""
import heapq

N = int(input())
maze = [list(map(int, list(input()))) for _ in range(N)]
cnt = [[100]*N for _ in range(N)]
cnt[0][0] = 0
heap = [(0, 0, 0)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

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
            if maze[ni][nj]:  # 다음 칸이 공짜네
                if now < cnt[ni][nj]:  # 갱신이 안되있네
                    cnt[ni][nj] = now
                    heapq.heappush(heap, (now, ni, nj))
            else:  # 다음칸이 벽이네
                if now + 1 < cnt[ni][nj]:
                    cnt[ni][nj] = now + 1
                    heapq.heappush(heap, (now + 1, ni, nj))
print(cnt[-1][-1])