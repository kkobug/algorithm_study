N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

ans = [0] * (K+1)

for i in range(N):
    temp = [0]*(K+1)
    for j in range(nums[i], K+1, nums[i]):
        temp[j] = 1

    print(temp)
    for k in range(nums[i], K+1):
        ans[k] += temp[k] + ans[k-nums[i]]

print(ans[K])