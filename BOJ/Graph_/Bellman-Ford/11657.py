"""
https://www.acmicpc.net/problem/11657
"""
from sys import stdin
input = stdin.readline


def is_loop():
    for i in range(N):
        for vertex in range(1, 1 + N):
            for next_vertex, next_cost in bus[vertex]:
                if dist[vertex] < 5000000 and dist[vertex] + next_cost < dist[next_vertex]:
                    dist[next_vertex] = dist[vertex] + next_cost
                    if i == N-1:
                        return True
    return False


N, M = map(int, input().split())
bus = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    bus[A].append([B, C])

dist = [5000000] * (N+1)
dist[1] = 0

if is_loop():
    print(-1)
else:
    for i in range(2, 1+N):
        if dist[i] < 5000000:
            print(dist[i])
        else:
            print(-1)
