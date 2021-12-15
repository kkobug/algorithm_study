"""
https://www.acmicpc.net/problem/17136
"""
from sys import stdin
input = stdin.readline


def dfs(idx, V, cnt, color):
    global ans
    if ans <= cnt:
        return
    if idx == L:
        ans = cnt
        return

    i, j = space[idx]

    if V[i][j]:
        dfs(idx+1, V, cnt, color)

    else:
        def sticky(x):
            if 0 < color[x-1] and i <= 10-x and j <= 10-x:
                flag = True
                for r in range(i, i+x):
                    for c in range(j, j+x):
                        if not paper[r][c] or V[r][c]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    for r in range(i, i+x):
                        for c in range(j, j+x):
                            V[r][c] = True
                    color[x-1] -= 1
                    dfs(idx, V, cnt, color)
                    color[x-1] += 1
                    for r in range(i, i+x):
                        for c in range(j, j+x):
                            V[r][c] = temp[r][c]
        temp = [[False]*10 for _ in range(10)]
        for r in range(10):
            for c in range(10):
                temp[r][c] = V[r][c]
        idx += 1
        cnt += 1
        sticky(5)
        sticky(4)
        sticky(3)
        sticky(2)
        if 0 < color[0]:
            V[i][j] = True
            color[0] -= 1
            dfs(idx, V, cnt, color)
            color[0] += 1
            V[i][j] = False
        idx -= 1
        cnt -= 1


paper = [list(map(int, input().split())) for _ in range(10)]
visit = [[False]*10 for _ in range(10)]
space = []
for i in range(10):
    for j in range(10):
        if paper[i][j]:
            space.append((i, j))
        else:
            visit[i][j] = True
L = len(space)
ans = 26
dfs(0, visit, 0, [5, 5, 5, 5, 5])
if ans == 26:
    ans = -1
print(ans)
