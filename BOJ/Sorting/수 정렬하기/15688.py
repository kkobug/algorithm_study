import heapq

N = int(input())
arr = []
heapq.heapify(arr)
for _ in range(N):
    i = int(input())
    heapq.heappush(arr, i)
print(arr)
for i in range(N):
    print(heapq.heappop(arr))