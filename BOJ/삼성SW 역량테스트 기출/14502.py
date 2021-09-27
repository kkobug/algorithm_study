"""
https://www.acmicpc.net/problem/14503
예제 입력
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력
9
"""
from copy import deepcopy
from sys import stdin as st

def dfs(K, G):
    while G:
        r, c = G.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and K[nr][nc] == 0:
                K[nr][nc] = 2
                G.append((nr, nc))
    cnt_zero = 0
    for r in range(N):
        for c in range(M):
            if K[r][c] == 0:
                cnt_zero += 1
    return cnt_zero


def spray(L, idx_x=0, idx_y=0, cnt=0):
    global ans
    if cnt == 3:
        temp = dfs(deepcopy(L), deepcopy(gas))
        if ans < temp:
            ans = temp
        return

    for x in range(idx_x, N):
        for y in range(M):
            if x == idx_x:
                if y < idx_y:
                    continue
            if L[x][y] == 0:
                L[x][y] = 1
                spray(L, x, y, cnt+1)
                L[x][y] = 0

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = map(int, st.readline().split())
lab = []
gas = []
ans = 0
for x in range(N):
    T = list(map(int, st.readline().split()))
    lab.append(T)
    for y in range(M):
        if T[y] == 2:
            gas.append((x, y))
spray(lab)
print(ans)