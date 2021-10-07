def dfs(r, c):
    V = [[False]*N for _ in range(N)]
    S = [(r, c)]
    V[r][c] = True
    cnt = 1
    while S:
        i, j = S.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if room[ni][nj] == room[i][j] + 1:
                    V[ni][nj] = True
                    S.append((ni, nj))
                    visit[room[ni][nj]] = True
                    cnt += 1
    return cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visit = [False]*(N*N+1)
    R = ans = 0
    for x in range(N):
        for y in range(N):
            if visit[room[x][y]]:
                continue
            temp = dfs(x, y)
            if ans == temp:
                R = min(R, room[x][y])
            elif ans < temp:
                ans = temp
                R = room[x][y]

    print(f'#{tc+1} {R} {ans}')