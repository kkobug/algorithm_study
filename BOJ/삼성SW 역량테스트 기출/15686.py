"""
https://www.acmicpc.net/problem/15686
"""
from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
home = []
shop = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            shop.append((i, j))
sel = combinations(shop, M)  # 완전탐색이 아닌, 단순 거리계산이므로 굳이 재귀함수를 돌 필요가 없다고 생각

ans = 2048
for S in sel:
    temp_ans = 0
    for X in home:
        temp = 100
        for Y in S:
            temp = min(temp, abs(X[0]-Y[0]) + abs(X[1]-Y[1]))
        temp_ans += temp
        if ans <= temp_ans: break
    ans = min(temp_ans, ans)
print(ans)
