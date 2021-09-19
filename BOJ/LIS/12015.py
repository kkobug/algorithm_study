import bisect

N = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]


for i in range(1, N):
    if nums[i-1] < nums[i]:
        dp.append(nums[i])
    else:
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]

print(len(dp))