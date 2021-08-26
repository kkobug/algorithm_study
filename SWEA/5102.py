def distance(st, ed):

    check = [st]
    visited = [-1] * (V+1)
    visited[st] = 0
    while check:
        now = check.pop()

        for j in range(V+1):
            if node[now][j] == 1:
                check.append(j)
                node[now][j] = 0
                visited[j] = visited[now] + 1

        if visited[ed] != -1: return visited[ed]

    return 0


for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())

    node = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int, input().split())
        node[x][y] = 1
        node[y][x] = 1

    s, e = map(int, input().split())
    print("#{} {}".format(tc, distance(s, e)))
