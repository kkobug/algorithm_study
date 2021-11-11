"""
https://www.acmicpc.net/problem/11779
"""
import heapq
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
city = [dict() for _ in range(N+1)]

for _ in range(M):
    st, ed, w = map(int, input().split())
    if city[st].get(ed):
        if w < city[st][ed]:
            city[st][ed] = w
    else:
        city[st][ed] = w

S, E = map(int, input().split())
cost = [float('inf')] * (N+1)
cost[S] = 0
heap = [(0, S, [S])]

while heap:
    now, st, path = heapq.heappop(heap)

    if st == E:
        print(now)
        print(len(path))
        print(*path)
        break

    if cost[st] < now:
        continue

    for ed, next_cost in city[st].items():
        total_cost = now + next_cost
        if total_cost < cost[ed]:
            cost[ed] = total_cost
            heapq.heappush(heap, (total_cost, ed, path + [ed]))