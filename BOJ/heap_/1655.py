"""
https://www.acmicpc.net/problem/1655
"""
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

# 중간값 보다 큰 값을 저장
min_heap = []
# 중간값 보다 작은 값을 저장
max_heap = []

N = int(input())

num = int(input())
heappush(max_heap, -num)
print(num)

for _ in range(N-1):
    num = int(input())
    if -max_heap[0] < num:
        heappush(min_heap, num)
    else:
        heappush(max_heap, -num)

    if len(max_heap) > len(min_heap)+1:
        heappush(min_heap, -heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heappush(max_heap, -heappop(min_heap))

    print(-max_heap[0])