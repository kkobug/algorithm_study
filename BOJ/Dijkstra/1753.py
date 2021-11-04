"""
https://www.acmicpc.net/problem/1753
"""
from sys import stdin
import heapq
input = stdin.readline

V, E = map(int, input().split())
K = int(input())
road = [dict() for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if road[u].get(v):
        if w < road[u][v]:
            road[u][v] = w
    else:
        road[u][v] = w

dist = [float('inf')] * (V+1)
dist[K] = 0
heap = []
heapq.heappush(heap, [0, K])
while heap:
    now, now_dist = heapq.heappop(heap)
    if dist[now_dist] < now:
        continue

    for next, next_dist in road[now_dist].items():
        new_dist = now + next_dist
        if new_dist < dist[next]:
            dist[next] = new_dist
            heapq.heappush(heap, [new_dist, next])

for i in range(1, 1+V):
    if dist[i] < float('inf'):
        print(dist[i])
    else:
        print('INF')
