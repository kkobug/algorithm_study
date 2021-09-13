"""
https://www.acmicpc.net/problem/14500
예제 입력 1
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1
19
"""
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
di = [
    [1, 0, 1], [0, 0, 0], [1, 2, 3],
    [0, 1, 2], [1, 2, 2], [1, 0, 0], [0, 0, -1],
    [-2, -1, 0], [1, 0, 0], [1, 1, 1], [2, 1, 0],
    [-1, -1, 0], [1, 1, 0], [2, 1, 1], [-1, 1, 0],
    [-1, 0, 1], [-1, 0, 1], [1, 1, 1], [1, 0, 0],
]
dj = [
    [1, 1, 0], [1, 2, 3], [0, 0, 0],
    [1, 1, 1], [0, 0, 1], [0, 1, 2], [1, 2, 2],
    [1, 1, 1], [2, 2, 1], [2, 1, 0], [0, 0, 1],
    [2, 1, 1], [2, 1, 1], [1, 1, 0], [1, 0, 1],
    [1, 1, 1], [0, 1, 0], [-1, 0, 1], [1, 2, 1],
]
for i in range(N):
    for j in range(M):
        for k in range(19):
            temp = board[i][j]
            for d in range(3):
                ni = i + di[k][d]
                nj = j + dj[k][d]
                if 0 <= ni < N and 0 <= nj < M:
                    temp += board[ni][nj]
                else:
                    break
            if ans < temp:
                ans = temp
print(ans)


















"""
import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
"""