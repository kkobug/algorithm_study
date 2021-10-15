from pprint import pprint
from collections import deque

for T in range(int(input())):
    N, M, X = map(int, input().split())
    home = [[] for _ in range(N+1)]
    dist = [[999999999]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        dist[x][y] = c
        home[x].append([y, c])

    for i in range(1, N+1):
        Q = deque([i])
        dist[i][i] = 0

        while Q:
            now = Q.popleft()

            for k in home[now]:
                ed, c = k
                d = dist[i][now] + c
                if d < dist[i][ed]:
                    dist[i][ed] = d
                    Q.append(ed)

    pprint(dist)
    ans = 0
    for i in range(N+1):
        a, b = dist[i][X], dist[X][i]
        if ans < a and a != 999999999:
            ans = a
        if ans < b and b != 999999999:
            ans = b
    print(ans)