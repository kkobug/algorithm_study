"""
https://programmers.co.kr/learn/courses/30/lessons/72413
"""
from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 200000000
    arr = [dict() for _ in range(1+n)]
    for st, ed, cost in fares:
        arr[st][ed] = cost
        arr[ed][st] = cost

    dist = [[200000000]*(1+n) for _ in range(1+n)]

    for i in range(1, 1+n):
        heap = [(0, i)]
        dist[i][i] = 0
        while heap:
            now_dist, now_point = heappop(heap)

            if dist[i][now_point] < now_dist:
                continue

            for next_point, next_dist in arr[now_point].items():
                total_dist = next_dist + now_dist
                if total_dist < dist[i][next_point]:
                    dist[i][next_point] = total_dist
                    heappush(heap, (total_dist, next_point))

    for i in range(1, 1+n):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer


print(solution(6, 4, 6, 2, [
    [4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]
]))
print(solution(7, 3, 4, 1, [
    [5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]
]))
print(solution(6, 4, 5, 6, [
    [2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]
]))
