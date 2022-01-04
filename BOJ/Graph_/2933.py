"""
https://www.acmicpc.net/problem/2933
"""
from sys import stdin
input = stdin.readline
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
R, C = map(int, input().split())
cave = []
for _ in range(R):
    cave.append(list(input()))


def check(x, y):
    visit = [[False]*C for _ in range(R)]
    stack = [(x, y)]
    mineral = [(x, y)]
    visit[x][y] = True
    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and not visit[ni][nj] and cave[ni][nj] == 'x':
                if ni == R-1:
                    return False
                visit[ni][nj] = True
                stack.append((ni, nj))
                mineral.append((ni, nj))

    down_cnt = 100
    for i, j in mineral:
        temp = how_many_down(i, j, visit)
        if temp and temp < down_cnt:
            down_cnt = temp
    for i, j in mineral:
        cave[i][j] = '.'
    for i, j in mineral:
        cave[i + down_cnt][j] = 'x'
    return True


def how_many_down(x, y, v):
    if x == R-1:
        return
    if v[x+1][y]:
        return
    cnt = 0
    while x < R-1:
        x += 1
        if cave[x][y] == '.' or v[x][y]:
            cnt += 1
        else:
            break
    return cnt


turn_cnt = int(input())
turn = list(map(int, input().split()))
for k in range(turn_cnt):
    i = R - turn[k]
    left = True
    if k % 2:
        left = False
        j = C-1
        while 0 <= j and cave[i][j] == '.':
            j -= 1
    else:
        j = 0
        while j < C and cave[i][j] == '.':
            j += 1
    if not 0 <= j < C:
        continue
    cave[i][j] = '.'
    cluster = False
    if i == 0:
        if left:
            if 0 <= j < C and cave[i][j+1] == 'x':
                cluster = check(i, j+1)
        else:
            if 0 <= j < C and cave[i][j-1] == 'x':
                cluster = check(i, j-1)
        if not cluster:
            if cave[i+1][j] == 'x':
                cluster = check(i+1, j)
    elif i == R-1:
        if left:
            if 0 <= j < C and cave[i][j + 1] == 'x':
                cluster = check(i, j + 1)
        else:
            if 0 <= j < C and cave[i][j - 1] == 'x':
                cluster = check(i, j - 1)
        if not cluster:
            if cave[i-1][j] == 'x':
                cluster = check(i-1, j)
    else:
        if left:
            if 0 <= j < C and cave[i][j + 1] == 'x':
                cluster = check(i, j + 1)
        else:
            if 0 <= j < C and cave[i][j - 1] == 'x':
                cluster = check(i, j - 1)
        if not cluster:
            if cave[i-1][j] == 'x':
                cluster = check(i-1, j)
        if not cluster:
            if cave[i + 1][j] == 'x':
                cluster = check(i + 1, j)

for _ in range(R):
    cave[_].pop()
    print(''.join(cave[_]))
