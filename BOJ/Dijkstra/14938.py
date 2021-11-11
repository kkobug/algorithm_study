"""
https://www.acmicpc.net/problem/14938
"""
from heapq import heappop, heappush
# 지역 수, 수색 범위, 길 개수
ans = 0
n, m, r = map(int, input().split())
# 지역별 아이템 수
field_items = list(map(int, input().split()))
# 지역
field = [dict() for _ in range(n+1)]
for _ in range(r):
    # 지역 번호 a <-> b, 거리
    a, b, l = map(int, input().split())
    # 이미 등록된 길이 있고 새 길이 더 짧으면 갱신 / 미등록길은 추가
    if field[a].get(b):
        if l < field[a][b]:
            field[a][b] = l
    else:
        field[a][b] = l

    if field[b].get(a):
        if l < field[b][a]:
            field[b][a] = l
    else:
        field[b][a] = l

# n번 다익스트라 시도
for i in range(1, n+1):
    dist = [float('inf')] * (n+1)
    dist[i] = 0
    heap = [(0, i)]
    while heap:
        # 간 거리, 지금 위치
        cost, now = heappop(heap)

        if dist[now] < cost:
            continue

        # 지금 위치에서 갈 수 있는 지점 검사
        for _next, next_cost in field[now].items():
            total_cost = cost + next_cost
            if m < total_cost:
                continue
            if total_cost < dist[_next]:
                dist[_next] = total_cost
                heappush(heap, (total_cost, _next))
    temp = 0
    for d in range(1, n+1):
        if dist[d] <= m:
            temp += field_items[d-1]
    if ans < temp:
        ans = temp
print(ans)
