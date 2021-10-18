import sys, bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
LIS = [sys.maxsize] * N
DP = [0] * N

for i in range(N):
    idx = bisect.bisect_left(LIS, arr[i])
    LIS[idx] = arr[i]
    DP[i] = idx

max_idx = bisect.bisect_left(LIS, sys.maxsize)
print(max_idx)

ans = []
end = max(DP)
for i in range(N - 1, -1, -1):
    if DP[i] == end:
        ans.append(arr[i])
        end -= 1
ans.reverse()
print(*ans)
