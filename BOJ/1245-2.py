N, M = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0
Q = [(0, 0)]

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        while Q:
            i, j = Q.pop(0)
            visited[i][j] = True

            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]

                if not (0 <= ni < N and 0 <= nj < M):
                    continue
                if visited[ni][nj]:
                    continue
                if mountain[ni][nj] <= mountain[i][j]:
                    Q.append((ni, nj))
        ans += 1

print(ans)