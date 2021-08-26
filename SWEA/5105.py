def bfs(r, c):
    visited = [(r, c)]

    while visited:
        r, c = visited.pop()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and (maze[nr][nc] == '0' or maze[nr][nc] == '3'):
                maze[nr][nc] = maze[r][c] + 1
                visited.append((nr, nc))

        if maze[ei][ej] != '3':
            return maze[ei][ej]-1

    return 0


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for tc in range(1, 1+int(input())):
    N = int(input())
    maze = []

    for i in range(N):
        maze.append(list(input()))
        for j in range(N):
            if maze[i][j] == '2':
                si, sj = i, j
                maze[si][sj] = 0
            elif maze[i][j] == '3':
                ei, ej = i, j

    print("#{} {}".format(tc, bfs(si, sj)))
