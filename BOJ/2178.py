from sys import stdin as st


N, M = map(int, st.readline().split())
maze = [list(st.readline()) for _ in range(N)]

i, j, num = 0, 0, 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [(i, j)]
stack = []
while maze[N-1][M-1] == '1':

    while visited:
        i, j = visited.pop()
        maze[i][j] = '0'

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1':
                stack.append((ni, nj))

    visited = stack[:]
    stack = []
    num += 1

print(num)




"""
N, M = map(int, st.readline().split())
maze = [list(st.readline()) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

maze[0][0] = 1
stack = [[0, 0]]
while stack:
    i, j = stack.pop(0)

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '1':
            stack.append([ni, nj])
            maze[ni][nj] = maze[i][j] + 1

print(maze[N-1][M-1])
"""