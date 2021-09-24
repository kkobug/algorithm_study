from pprint import pprint
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
ground = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    trees[x][y].append(z)

for _ in range(K):
    # 봄 ~ 여름
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                tree = 0
                flag = True
                while tree < len(trees[i][j]):
                    if trees[i][j][tree] <= ground[i][j] and flag:
                        ground[i][j] -= trees[i][j][tree]  # 양분먹기
                        trees[i][j][tree] += 1  # 나이먹기
                        tree += 1
                    else:
                        flag = False
                        ground[i][j] += trees[i][j].pop(tree)//2  # 양분되기

    # 가을
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if not tree % 5:
                        for d in range(8):
                            ni = i + di[d]
                            nj = j + dj[d]
                            if 0 <= ni < N and 0 <= nj < N:
                                trees[i][j].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]
            if trees[i][j]:
                trees[i][j].sort()

ans = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            ans += len(trees[i][j])
pprint(trees)
print(ans)
