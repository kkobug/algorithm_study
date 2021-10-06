"""
https://www.acmicpc.net/problem/15685
예제 입력
3
3 3 0 1
4 2 1 3
4 2 2 1
예제 출력
4
"""
from sys import stdin
input = stdin.readline

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
grid = [[False]*101 for _ in range(101)]
ans = 0
for _ in range(int(input())):
    c, r, d, g = map(int, input().split())
    grid[r][c] = True
    dirs = [d]  # 시작점, 0세대 찍기
    nr = r + dr[d]
    nc = c + dc[d]
    grid[nr][nc] = True
    r, c = nr, nc

    for _ in range(g):  # 1세대 이상이면
        n_dirs = []  # 이번 세대에서 나갈 방향들
        for i in range(len(dirs)-1, -1, -1):
            n_dirs.append((dirs[i]+1)%4)

        for d in n_dirs:
            nr = r + dr[d]
            nc = c + dc[d]
            grid[nr][nc] = True
            r, c = nr, nc

        dirs += n_dirs

for r in range(100):
    for c in range(100):
        if grid[r][c] and grid[r+1][c] and grid[r][c+1] and grid[r+1][c+1]:
            ans += 1

print(ans)