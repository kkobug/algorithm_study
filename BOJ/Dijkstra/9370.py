"""
https://www.acmicpc.net/problem/9370
"""
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def dijkstra(st):
    heap = [(0, st)]
    dist = [int(1e9)] * (1 + n)
    dist[st] = 0
    while heap:
        now_dist, now_vertex = heappop(heap)

        if dist[now_vertex] < now_dist:
            continue

        for next_vertex, next_dist in road[now_vertex]:
            total_dist = now_dist + next_dist
            if total_dist < dist[next_vertex]:
                dist[next_vertex] = total_dist
                heappush(heap, (total_dist, next_vertex))
    return dist


for __ in range(int(input())):
    # 교차로, 도로, 목적지 개수
    n, m, t = map(int, input().split())
    # 출발지, 지나는 지점
    s, g, h = map(int, input().split())
    road = [[] for _ in range(1+n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        road[a].append([b, d])
        road[b].append([a, d])
        if (a, b) == (g, h) or (a, b) == (h, g):
            required_cost = d

    main_dist = dijkstra(s)
    h_dist = dijkstra(h)
    g_dist = dijkstra(g)
    ans = []
    for _ in range(t):
        target = int(input())
        g_need_dist = main_dist[g] + required_cost + h_dist[target]
        h_need_dist = main_dist[h] + required_cost + g_dist[target]
        if main_dist[target] in (g_need_dist, h_need_dist):
            ans.append(target)
    ans.sort()
    print(*ans)