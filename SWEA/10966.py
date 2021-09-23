dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    pool = [list(input()) for _ in range(N)]
    distance = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                visited = [[False]*M for _ in range(N)]
                Q = [(i, j)]
                visited[i][j] = False
                while Q:
                    r, c = Q.pop(0)
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False:
                            if distance[nr][nc] != 0 and distance[r][c] >= distance[nr][nc]:
                                continue
                            if pool[nr][nc] == 'L' or distance[r][c] < distance[nr][nc]:
                                Q.append((nr, nc))
                                visited[nr][nc] = True
                                distance[nr][nc] = distance[r][c] + 1

    print(f'#{tc} {sum(map(sum, distance))}')