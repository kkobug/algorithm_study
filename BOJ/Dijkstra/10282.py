"""
https://www.acmicpc.net/problem/10282
"""
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

for tc in range(int(input())):
    n, d, c = map(int, input().split())
    cpu = [dict() for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        cpu[b][a] = s

    time = [float('inf')] * (n+1)
    time[c] = 0
    heap = [(0, c)]
    while heap:
        now_time, now_cpu = heappop(heap)

        if time[now_cpu] < now_time:
            continue

        for next_cpu, next_time in cpu[now_cpu].items():
            total_time = next_time + now_time
            if total_time < time[next_cpu]:
                time[next_cpu] = total_time
                heappush(heap, (total_time, next_cpu))

    cpu_cnt = infection_time = 0
    for i in range(1, n+1):
        if time[i] < float('inf'):
            cpu_cnt += 1
            if infection_time < time[i]:
                infection_time = time[i]

    print(cpu_cnt, infection_time)
