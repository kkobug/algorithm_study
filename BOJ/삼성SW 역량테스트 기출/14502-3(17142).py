"""
https://www.acmicpc.net/problem/17142
예제 입력
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1
예제 출력
0
"""
from collections import deque
from copy import deepcopy

def bfs(L, V):
    while V:
        r, c = V.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and L[nr][nc] == 0:
                L[nr][nc] = L[r][c] + 1
                V.append((nr, nc))

    mini = 100000
    maxi = 2
    for a in range(N):
        for b in range(N):
            if (a, b) in virus:
                continue
            mini = min(L[a][b], mini)
            maxi = max(L[a][b], maxi)

    return maxi - 2, mini


def spray(idx=0, cnt=0, Q=deque()):
    global ans

    if cnt == M:
        temp = bfs(deepcopy(lab), deepcopy(Q))
        if temp[1] and temp[0] < ans:
            ans = temp[0]
        return

    for i in range(idx, len(virus)):
        Q.append(virus[i])
        lab[virus[i][0]][virus[i][1]] = 2
        spray(i+1, cnt+1, Q)
        lab[virus[i][0]][virus[i][1]] = 0
        Q.pop()


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M = map(int, input().split())
lab = []
virus = []
for i in range(N):
    temp = list(map(int, input().split()))
    lab.append(temp)
    for j in range(N):
        if temp[j] == 2:
            virus.append((i, j))
            lab[i][j] = 0

ans = 10000
spray()
if ans == 10000:
    print(-1)
else:
    print(ans)