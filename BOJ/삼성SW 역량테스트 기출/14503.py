"""
https://www.acmicpc.net/problem/14503
예제 입력
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력
1
"""
def dfs(i, j, d):
    global ans
    for _ in range(4):
        d = (d-1)%4
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:
            room[ni][nj] = 2
            dfs(ni, nj, d)
            ans += 1
            break
    else:
        d = (d-2)%4
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if room[ni][nj] == 2:
                dfs(ni, nj, (d-2)%4)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
R, C, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
room[R][C] = 2

ans = 1
dfs(R, C, D)
print(ans)