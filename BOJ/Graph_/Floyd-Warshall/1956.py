"""
https://www.acmicpc.net/problem/1956
"""
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

V, E = map(int, input().split())
road = [dict() for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    road[a][b] = c

ans = 4000000
dist = [[4000000]*(V+1) for _ in range(V+1)]

for i in range(1, V+1):
    heap = [(0, i)]
    dist[i][i] = 0
    flag = True
    while heap and flag:
        now_dist, now_city = heappop(heap)

        if dist[i][now_city] < now_dist:
            continue

        for next_city, next_dist in road[now_city].items():
            total_dist = next_dist + now_dist
            if next_city == i:
                if total_dist < ans:
                    ans = total_dist
                    flag = False
            if total_dist < dist[i][next_city]:
                dist[i][next_city] = total_dist
                heappush(heap, (total_dist, next_city))

if ans == 4000000:
    ans = -1
print(ans)
