import bisect

N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N
LIS = [nums[0]]

for i in range(1, N):
    if nums[i-1] < nums[i]:
        dp[i] = dp[i-1] + 1
        LIS.append(nums[i])
    elif nums[i-1] > nums[i]:
        idx = bisect.bisect_left(LIS, nums[i])
        LIS[idx] = nums[i]
        dp[i] = dp[idx-1]

max_idx = max(dp)
print(max_idx)
ans = []

for i in range(max_idx, -1, -1):
    if dp[i] == max_idx:
        ans.append(nums[i])
        max_idx -= 1

ans.reverse()
print(*ans)