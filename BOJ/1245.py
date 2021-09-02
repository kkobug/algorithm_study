from sys import stdin as st


di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
N, M = map(int, st.readline().split())
mountain = [list(map(int, st.readline().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if check[i][j]: continue

        flag = False
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < M:
                if mountain[ni][nj] > mountain[i][j]:
                    flag = True
                    break
        if flag: continue

        stack = []
        stack.append((i, j))
        while stack:
            x, y = stack.pop()
            check[x][y] = True

            flag2 = True
            for d in range(8):
                nx = x + di[d]
                ny = y + dj[d]

                if 0 <= nx < N and 0 <= ny < M:
                    if mountain[nx][ny] == mountain[x][y] and not check[nx][ny]:
                        stack.append((nx, ny))

                    elif mountain[nx][ny] > mountain[x][y]:
                        flag2 = False
                        break

            if not flag2: break
        if flag2: cnt += 1

print(cnt)
