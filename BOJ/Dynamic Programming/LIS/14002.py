N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

max_idx = max(dp)
print(max_idx)
idx = dp.index(max_idx)
ans = []

for i in range(idx, -1, -1):
    if dp[i] == max_idx:
        ans.append(nums[i])
        max_idx -= 1
ans.reverse()
print(*ans)
