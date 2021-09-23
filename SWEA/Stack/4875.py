import time
"""
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
"""


# DFS with stack
def DFS(M, i, j):
    stack = [[i, j]]
    visited = []

    while stack and M[i][j] != 3:
        visited.append([i, j])
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if M[ni][nj] != 1 and [ni, nj] not in visited:
                stack.append([ni, nj])

        if stack[-1][0] == i and stack[-1][1] == j:
            i, j = stack.pop()
        else:
            i, j = stack[-1][0], stack[-1][1]

    if stack:
        return 1
    return 0


# Backtracking
def backtracking(i, j):
    global ans

    if maps[i][j] == 3:
        ans = 1
        return ans

    maps[i][j] = 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if maps[ni][nj] != 1:
            backtracking(ni, nj)
    maps[i][j] = 0  # 이거 없으면 지나온길 때문에 길이 막힐 수 있음.. 복구시켜놔야함 (이 문제에서는 해당하는 경우 없음)


for tc in range(1, 1+int(input().strip())):
    N = int(input().strip())
    maps = [[1] * (N+2)]  # 주변에 1 둘러서 받기
    for i in range(N):
        miro = list(map(int, input().strip()))
        maps.append([1] + miro + [1])
        for j in range(N):
            if miro[j] == 2:
                st_i, st_j = i+1, j+1
    maps.append([1] * (N+2))

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    ans = 0
    backtracking(st_i, st_j)
    print("#{} {}".format(tc, ans))
    # print("#{} {}".format(tc, DFS(maps, st_i, st_j)))