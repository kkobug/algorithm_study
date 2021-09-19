"""
https://www.acmicpc.net/problem/1245
예제 입력 1
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0
예제 출력 1
3
"""
N, M = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
ans = 0
Q = []

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(M):
        flag = True
        if visited[i][j]:
            continue
        Q.append((i, j))
        while Q:
            r, c = Q.pop(0)
            visited[r][c] = True

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    if mountain[r][c] == mountain[nr][nc] and not visited[nr][nc]:
                        Q.append((nr, nc))
                        visited[nr][nc] = True
                    elif flag and mountain[r][c] < mountain[nr][nc]:
                        flag = False

        if flag:
            ans += 1

print(ans)
