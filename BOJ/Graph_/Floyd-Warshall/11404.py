"""
https://www.acmicpc.net/problem/11404
"""
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

N = int(input())
M = int(input())
bus = [dict() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if bus[a].get(b):
        if c < bus[a][b]:
            bus[a][b] = c
    else:
        bus[a][b] = c

dist = [[10000000]*(N+1) for _ in range(N+1)]
for i in range(1, 1+N):
    dist[i][i] = 0

for i in range(1, 1+N):
    heap = [(0, i)]
    while heap:
        now_cost, now_vertex = heappop(heap)

        if dist[i][now_vertex] < now_cost:
            continue

        for next_vertex, next_cost in bus[now_vertex].items():
            total_cost = now_cost + next_cost
            if total_cost < dist[i][next_vertex]:
                dist[i][next_vertex] = total_cost
                heappush(heap, (total_cost, next_vertex))

for i in range(1, 1+N):
    for j in range(1, 1+N):
        if dist[i][j] == 10000000:
            dist[i][j] = 0
    print(*dist[i][1:])
