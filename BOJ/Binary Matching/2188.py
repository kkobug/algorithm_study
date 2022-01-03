"""
https://www.acmicpc.net/problem/2188
"""
from sys import stdin
input = stdin.readline


def match(k):
    if visit[k]:
        return
    visit[k] = True
    for j in cow[k]:
        if not home[j] or match(home[j]):
            home[j] = k
            return True
    return


N, M = map(int, input().split())
home = [0] * (M+1)
cow = [[]]
for _ in range(N):
    cow.append(list(map(int, input().split()))[1:])

ans = 0
for i in range(1, 1+N):
    visit = [False] * (N+1)
    if match(i):
        ans += 1

print(ans)