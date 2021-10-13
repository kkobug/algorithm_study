"""
https://www.acmicpc.net/problem/16234
예제 입력
2 20 50
50 30
20 40
예제 출력
1
"""
from sys import stdin
input = stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, L, R = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
flag = True
ans = 0

while flag:
    flag = False
    V = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if V[i][j]:
                continue
            union = [(i, j)]
            union_s = city[i][j]
            S = [(i, j)]
            V[i][j] = True
            while S:
                r, c = S.pop()
                for d in range(4):
                    ni = r + di[d]
                    nj = c + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and not V[ni][nj] and L <= abs(city[r][c] - city[ni][nj]) <= R:
                        S.append((ni, nj))
                        union.append((ni, nj))
                        union_s += city[ni][nj]
                        V[ni][nj] = True
                        if not flag and city[r][c] != city[ni][nj]:
                            flag = True
            union_s //= len(union)
            for u in union:
                city[u[0]][u[1]] = union_s
    if flag:
        ans += 1

print(ans)