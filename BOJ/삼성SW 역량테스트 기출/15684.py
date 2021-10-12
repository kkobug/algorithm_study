"""
https://www.acmicpc.net/problem/15684
"""
from sys import stdin
input = stdin.readline


def game(F, cnt=0, idx=0):
    global ans
    if -1 < ans:
        return
    if cnt == F:
        for c in range(N-1):
            j = c
            for i in range(H):
                j += L[i][j]
            if j != c:
                break
        else:
            ans = F
        return
    for p in range(idx, len(L_add)):
        i, j = L_add[p]
        if L[i][j] or L[i][j+1]:
            continue
        L[i][j] = 1
        L[i][j+1] = -1
        game(F, cnt+1, idx+1)
        L[i][j] = L[i][j+1] = 0


N, M, H = map(int, input().split())
L = [[0]*N for _ in range(H)]
L_add = []

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    L[i][j] = 1
    L[i][j+1] = -1

for i in range(H):
    for j in range(N-1):
        if L[i][j] or L[i][j+1]:
            continue
        L_add.append((i, j))

ans = -1
if L_add:
    for k in range(min(len(L_add)+1, 4)):
        game(k)
        if -1 < ans:
            break
else:
    game(0)

print(ans)