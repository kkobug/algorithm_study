"""
https://www.acmicpc.net/problem/1504
"""
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

N, E = map(int, input().split())
graph = [dict() for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    if graph[a].get(b):
        if c < graph[a][b]:
            graph[a][b] = c
    else:
        graph[a][b] = c

    if graph[b].get(a):
        if c < graph[b][a]:
            graph[b][a] = c
    else:
        graph[b][a] = c

v1, v2 = map(int, input().split())

# 시작점은 1, 종점은 N, v1과 v2 중 어느곳을 먼저갈지는 몰라
# 1 -> v1 -> v2 -> N // 1 -> v2 -> v1 -> N
# 3번의 탐색을 2번 반복해야...

def dijkstra(st, ed):
    dist = [float('inf')] * (N+1)
    dist[st] = 0
    heap = [(0, st)]

    while heap:
        cost, now = heappop(heap)

        if now == ed:
            break

        if dist[now] < cost:
            continue

        for _next, next_cost in graph[now].items():
            total_cost = cost + next_cost
            if total_cost < dist[_next]:
                dist[_next] = total_cost
                heappush(heap, (total_cost, _next))
    return dist[ed]


mid = dijkstra(v1, v2)
ans1 = dijkstra(1, v1) + dijkstra(v2, N)
ans2 = dijkstra(1, v2) + dijkstra(v1, N)
ans = min(ans1, ans2) + mid
if ans < float('inf'):
    print(ans)
else:
    print(-1)
