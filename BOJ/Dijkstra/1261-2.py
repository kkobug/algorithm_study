import heapq

M, N = map(int, input().split())
room = [list(map(int, list(input()))) for _ in range(N)]
cnt = [[10000]*M for _ in range(N)]
heap = [(0, 0, 0)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

while heap:
    now, i, j = heapq.heappop(heap)
    if (i, j) == (N-1, M-1):
        break

    if cnt[i][j] < now:
        continue

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if room[ni][nj]:
                if now+1 < cnt[ni][nj]:
                    cnt[ni][nj] = now+1
                    heapq.heappush(heap, (now+1, ni, nj))
            elif now < cnt[ni][nj]:
                cnt[ni][nj] = now
                heapq.heappush(heap, (now, ni, nj))

print(cnt[-1][-1])