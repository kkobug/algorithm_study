"""
https://www.acmicpc.net/problem/1981
"""
from sys import stdin
input = stdin.readline


def dfs(l, r):
    stack = [(0, 0)]
    visit = [[False]*N for _ in range(N)]
    visit[0][0] = True
    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and l <= arr[ni][nj] <= r:
                if (ni, nj) == (N-1, N-1):
                    return True
                visit[ni][nj] = True
                stack.append((ni, nj))


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = []
left_st = 200
right_ed = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] < left_st:
            left_st = arr[i][j]
        if arr[i][j] > right_ed:
            right_ed = arr[i][j]
left_ed = min(arr[0][0], arr[-1][-1])
right_st = max(arr[0][0], arr[-1][-1])

left, right = left_st, right_st
ans = 200
while left_st <= left <= left_ed and right_st <= right <= right_ed:
    if dfs(left, right):
        ans = min(ans, right - left)
        left += 1
    else:
        right += 1

print(ans)
