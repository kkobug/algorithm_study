"""
https://www.acmicpc.net/problem/1865
"""
from sys import stdin
input = stdin.readline


def is_loop():
    dist = [5000000] * (N+1)
    for i in range(N):
        for vertex in range(1, 1+N):
            for next_vertex, next_cost in hole[vertex]:
                if dist[vertex] + next_cost < dist[next_vertex]:
                    dist[next_vertex] = dist[vertex] + next_cost
                    if i == N-1:
                        return True
    return False


for tc in range(int(input())):
    N, M, W = map(int, input().split())
    hole = [[] for _ in range(1+N)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        hole[S].append([E, T])
        hole[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        hole[S].append([E, -T])
    print("YES" if is_loop() else "NO")
