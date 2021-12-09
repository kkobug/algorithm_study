"""
https://www.acmicpc.net/problem/17070
"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

horizontal = [[0]*N for _ in range(N)]
vertical = [[0]*N for _ in range(N)]
diagonal = [[0]*N for _ in range(N)]

for i in range(1, N):
    if arr[0][i]:
        break
    horizontal[0][i] = 1

for i in range(1, N):
    for j in range(2, N):
        if not arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
            diagonal[i][j] = diagonal[i-1][j-1] + horizontal[i-1][j-1] + vertical[i-1][j-1]

        if not arr[i][j]:
            horizontal[i][j] = horizontal[i][j-1] + diagonal[i][j-1]
        if not arr[i][j]:
            vertical[i][j] = vertical[i-1][j] + diagonal[i-1][j]

print(horizontal[-1][-1]+vertical[-1][-1]+diagonal[-1][-1])