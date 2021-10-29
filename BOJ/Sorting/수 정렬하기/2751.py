"""
https://www.acmicpc.net/problem/2751
"""
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    L = merge_sort(nums[:mid])
    R = merge_sort(nums[mid:])

    ret = []
    idx_L = idx_R = 0
    len_L, len_R = len(L), len(R)

    while idx_L < len_L and idx_R < len_R:
        if L[idx_L] < R[idx_R]:
            ret.append(L[idx_L])
            idx_L += 1
        else:
            ret.append(R[idx_R])
            idx_R += 1
    while idx_L < len_L:
        ret.append(L[idx_L])
        idx_L += 1
    while idx_R < len_R:
        ret.append(R[idx_R])
        idx_R += 1
    return ret

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr = merge_sort(arr)
for i in arr:
    print(i)