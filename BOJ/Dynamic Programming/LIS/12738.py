import bisect

N = int(input())
nums = list(map(int, input().split()))
LIS = [nums[0]]


for i in range(1, N):
    if LIS[-1] < nums[i]:
        LIS.append(nums[i])
    else:
        idx = bisect.bisect_left(LIS, nums[i])
        LIS[idx] = nums[i]

print(len(LIS))