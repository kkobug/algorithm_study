"""
https://www.acmicpc.net/problem/17135
"""
from copy import deepcopy
from collections import deque
from sys import stdin
input = stdin.readline
di = [0, -1, 0]
dj = [-1, 0, 1]


def game(a):
    flag = True
    now = deque(deepcopy(arr))
    cnt = 0
    while flag:
        catch_list = set()
        for i, j in a:
            visit = [[False]*M for _ in range(N)]
            not_catch = True
            Q = deque()
            Q.append((i, j))
            while Q and not_catch:
                r, c = Q.popleft()
                for d in range(3):
                    ni = r + di[d]
                    nj = c + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
                        visit[ni][nj] = True
                        if D < abs(ni-i) + abs(nj-j):
                            continue
                        if now[ni][nj]:
                            not_catch = False
                            catch_list.add((ni, nj))
                            break
                        else:
                            Q.append((ni, nj))
        for i, j in catch_list:
            cnt += 1
            now[i][j] = 0
        now.pop()
        now.appendleft([0]*M)
        if not sum(map(sum, now)):
            flag = False
    return cnt


def comb(idx, A):
    global ans
    if len(A) == 3:
        cnt = game(A)
        if ans < cnt:
            ans = cnt
        return

    for i in range(idx, len(archer)):
        A.append(archer[i])
        comb(i+1, A)
        A.pop()


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
archer = [(N, _) for _ in range(M)]
ans = 0
comb(0, [])
print(ans)