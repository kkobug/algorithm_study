"""
https://www.acmicpc.net/problem/1238
"""
import heapq

def dijkstra(my_dist, my, X):
    heap = []
    heapq.heappush(heap, [0, X])
    while heap:
        dist, now = heapq.heappop(heap)
        if my_dist[now] < dist:
            continue
        for next_node, next_dist in my[now]:
            new_dist = dist + next_dist
            if new_dist < my_dist[next_node]:
                my_dist[next_node] = new_dist
                heapq.heappush(heap, [new_dist, next_node])

N, M, X = map(int, input().split())
go = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]
for _ in range(M):
    st, ed, T = map(int, input().split())
    go[st].append([ed, T])
    back[ed].append([st, T])

go_dist = [float('inf')]*(N+1)
back_dist = [float('inf')]*(N+1)
go_dist[X] = back_dist[X] = 0

dijkstra(go_dist, go, X)
dijkstra(back_dist, back, X)

ans = 0
for i in range(1, N+1):
    ans = max(ans, go_dist[i] + back_dist[i])
print(ans)