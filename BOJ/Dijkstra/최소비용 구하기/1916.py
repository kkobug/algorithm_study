"""
https://www.acmicpc.net/problem/1916
"""
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
city = [dict() for _ in range(N+1)]
for _ in range(M):
    st, ed, cost = map(int, input().split())
    if type(city[st].get(ed)) == int:
        if cost < city[st][ed]:
            city[st][ed] = cost
    else:
        city[st][ed] = cost

A, B = map(int, input().split())
dist = [float('inf')] * (N+1)
dist[A] = 0
heap = [(0, A)]
while heap:
    cost, now = heappop(heap)

    if now == B:
        break

    if dist[now] < cost:
        continue

    for _next, next_cost in city[now].items():
        total_cost = next_cost + cost
        if total_cost < dist[_next]:
            dist[_next] = total_cost
            heappush(heap, (total_cost, _next))

print(dist[B])
