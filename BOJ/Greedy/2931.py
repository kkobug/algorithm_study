"""
https://www.acmicpc.net/problem/2931
"""
from sys import stdin
input = stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

R, C = map(int, input().split())
visit = [[0]*C for _ in range(R)]
pipe = []
moscow = (0, 0)
zagreb = (0, 0)

for i in range(R):
    temp = list(input())
    pipe.append(temp)
    for j in range(C):
        if temp[j] == "+":
            visit[i][j] = -1
        elif temp[j] == "M":
            moscow = (i, j)
        elif temp[j] == "Z":
            zagreb = (i, j)

i, j = moscow
next_i = next_j = False
for d in range(4):
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < R and 0 <= nj < C:
        if pipe[ni][nj] == ".":
            continue
        if d == 0:
            if pipe[ni][nj] in ["-", "+", "3", "4"]:
                next_i, next_j = ni, nj
        elif d == 1:
            if pipe[ni][nj] in ["|", "+", "2", "3"]:
                next_i, next_j = ni, nj
        elif d == 2:
            if pipe[ni][nj] in ["-", "+", "1", "2"]:
                next_i, next_j = ni, nj
        elif d == 3:
            if pipe[ni][nj] in ["|", "+", "1", "4"]:
                next_i, next_j = ni, nj

ans = []
ans_list = []
stack = [(i, j, next_i, next_j)]
while stack:
    now_i, now_j, next_i, next_j = stack.pop()
    visit[now_i][now_j] += 1
    if pipe[next_i][next_j] == "-":
        if now_j < next_j:
            stack.append((next_i, next_j, next_i, next_j+1))
        else:
            stack.append((next_i, next_j, next_i, next_j-1))
    elif pipe[next_i][next_j] == "|":
        if now_i < next_i:
            stack.append((next_i, next_j, next_i+1, next_j))
        else:
            stack.append((next_i, next_j, next_i-1, next_j))
    elif pipe[next_i][next_j] == "1":
        if now_j == next_j:
            stack.append((next_i, next_j, next_i, next_j+1))
        else:
            stack.append((next_i, next_j, next_i+1, next_j))
    elif pipe[next_i][next_j] == "2":
        if now_j == next_j:
            stack.append((next_i, next_j, next_i, next_j+1))
        else:
            stack.append((next_i, next_j, next_i-1, next_j))
    elif pipe[next_i][next_j] == "3":
        if now_j == next_j:
            stack.append((next_i, next_j, next_i, next_j-1))
        else:
            stack.append((next_i, next_j, next_i-1, next_j))
    elif pipe[next_i][next_j] == "4":
        if now_j == next_j:
            stack.append((next_i, next_j, next_i, next_j-1))
        else:
            stack.append((next_i, next_j, next_i+1, next_j))
    elif pipe[next_i][next_j] == "+":
        if now_j == next_j:
            if now_i < next_i:
                stack.append((next_i, next_j, next_i+1, next_j))
            else:
                stack.append((next_i, next_j, next_i-1, next_j))
        else:
            if now_j < next_j:
                stack.append((next_i, next_j, next_i, next_j+1))
            else:
                stack.append((next_i, next_j, next_i, next_j-1))
    elif pipe[next_i][next_j] == ".":
        ans = [next_i+1, next_j+1]
        for d in range(4):
            ni = next_i + di[d]
            nj = next_j + dj[d]
            if 0 <= ni < R and 0 <= nj < C:
                if 0 < visit[ni][nj]:
                    continue
                if pipe[ni][nj] == ".":
                    continue
                if (ni, nj) == (now_i, now_j):
                    continue
                if d == 0:
                    if pipe[ni][nj] in ["-", "+", "3", "4"]:
                        ans_list.append((ni, nj))
                elif d == 1:
                    if pipe[ni][nj] in ["|", "+", "2", "3"]:
                        ans_list.append((ni, nj))
                elif d == 2:
                    if pipe[ni][nj] in ["-", "+", "1", "2"]:
                        ans_list.append((ni, nj))
                elif d == 3:
                    if pipe[ni][nj] in ["|", "+", "1", "4"]:
                        ans_list.append((ni, nj))
        if 1 < len(ans_list):
            ans.append("+")
        else:
            i, j = ans_list.pop()
            if i == now_i:
                ans.append("-")
            elif j == now_j:
                ans.append("|")
            else:
                if j - i == now_j - now_i:
                    if next_i < now_i or now_j < next_j:
                        ans.append("4")
                    elif now_i < next_i or next_j < now_j:
                        ans.append("2")
                else:
                    if next_i < now_i or next_j < now_j:
                        ans.append("1")
                    elif now_i < next_i or now_j < next_j:
                        ans.append("3")
print(" ".join(map(str, ans)))
