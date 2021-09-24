# def gohome(k):
#     if check[k]:
#         return
#
#     for j in cows[k][1:]:
#         if not home[k] or gohome(home[k]):
#             home[k] = cows[k][0]
#             return
#     return
#
#
# N, M = map(int, input().split())
# cows = [[]]
# home = [0] * (M+1)
#
# for i in range(N):
#     cows.append([i+1] + list(map(int, input().split()))[1:])
#
# for i in range(N):
#     check = [False] * 201
#     gohome(i+1)
#
# print(home)

import sys
input = sys.stdin.readline


def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


n, m = map(int, input().split())
s = [[] for _ in range(n + 1)]
d = [0 for _ in range(m + 1)]
cnt = 0
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in a[1:]:
        s[i].append(j)
for i in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    if dfs(i):
        cnt += 1
print(d)
print(cnt)