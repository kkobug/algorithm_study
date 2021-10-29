"""
https://www.acmicpc.net/problem/2470
"""
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    L = merge_sort(nums[:mid])
    R = merge_sort(nums[mid:])

    ret = []
    len_L, len_R = len(L), len(R)
    idx_L = idx_R = 0
    while idx_L < len_L or idx_R < len_R:
        if idx_L < len_L and idx_R < len_R:
            if L[idx_L] < R[idx_R]:
                ret.append(L[idx_L])
                idx_L += 1
            else:
                ret.append(R[idx_R])
                idx_R += 1
        elif idx_L < len_L:
            ret.append(L[idx_L])
            idx_L += 1
        elif idx_R < len_R:
            ret.append(R[idx_R])
            idx_R += 1
    return ret

N = int(input())
acidity = merge_sort(list(map(int, input().split())))
ans_L = L = 0
ans_R = R = N-1
ans = abs(acidity[L] + acidity[R])
while L < R:
    temp = acidity[L] + acidity[R]
    if abs(temp) < ans:
        ans = abs(temp)
        ans_L = L
        ans_R = R
        if ans == 0:
            break
    if temp < 0:
        L += 1
    else:
        R -= 1

print(acidity[ans_L], acidity[ans_R])