from copy import deepcopy

def bfs(L, V):
    while V:
        r, c = V.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and L[nr][nc] == 0:
                L[nr][nc] = L[r][c] + 1
                V.append((nr, nc))

    mini = 100000
    maxi = 0
    for a in range(N):
        mini = min(min(L[a]), mini)
        maxi = max(max(L[a]), maxi)

    if mini == 0:
        return 0
    else:
        return maxi - 2


def spray(idx=0, cnt=0, Q=[]):
    global ans

    if cnt == M:
        temp = bfs(deepcopy(lab), deepcopy(Q))
        if temp:
            if temp < ans:
                ans = temp
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