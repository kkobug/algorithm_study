"""
https://www.acmicpc.net/problem/12930
"""
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

N = int(input())
weight1 = [[0]*N for _ in range(N)]
weight2 = [[0]*N for _ in range(N)]
for i in range(N):
    temp = list(input())
    for j in range(N):
        if temp[j] == '.':
            continue
        weight1[i][j] = int(temp[j])

for i in range(N):
    temp = list(input())
    for j in range(N):
        if temp[j] == '.':
            continue
        weight2[i][j] = int(temp[j])

dist = [[float('inf')]*N for _ in range(N)]
dist[0][0] = 0
heap = [(0, 0, 0, 0)]  # 코스트, c1, c2, vertex
while heap:
    now_cost, c1, c2, now_vertex = heappop(heap)
    for i in range(N):
        if not weight1[now_vertex][i]:
            continue
        nc1, nc2 = c1+weight1[now_vertex][i], c2+weight2[now_vertex][i]
        total_cost = nc1*nc2
        if total_cost < dist[now_vertex][i]:
            dist[now_vertex][i] = total_cost
            heappush(heap, (total_cost, nc1, nc2, i))

ans = float('inf')
for i in range(N):
    if dist[i][1] < ans:
        ans = dist[i][1]
if ans < float('inf'):
    print(ans)
else:
    print(-1)