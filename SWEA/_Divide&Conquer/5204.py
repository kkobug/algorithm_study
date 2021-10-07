def merge_sort(nums):
    global ans
    if len(nums) <= 1:
        return nums

    # 분할하기
    mid = len(nums) // 2
    L = merge_sort(nums[:mid])
    R = merge_sort(nums[mid:])

    # 여기부터 병합
    if L[-1] > R[-1]: ans += 1

    ret = []  # 병합한거 담기
    len_L, len_R = len(L), len(R)
    idx_L = idx_R = 0
    while idx_L < len_L or idx_R < len_R:
        if idx_L < len_L and idx_R < len_R:  # 둘다 담을거 있으면
            if L[idx_L] < R[idx_R]:  # 작은 것부터 골라담기
                ret.append(L[idx_L])
                idx_L += 1
            else:
                ret.append(R[idx_R])
                idx_R += 1

        elif idx_L < len_L:  # 왼쪽/오른쪽 중 남은 값들 처리
            ret.append(L[idx_L])
            idx_L += 1
        elif idx_R < len_R:
            ret.append(R[idx_R])
            idx_R += 1
    return ret


for tc in range(1, 1+int(input())):
    ans = 0
    N = int(input())
    arr = merge_sort(list(map(int, input().split())))

    print(f'#{tc} {arr[N//2]} {ans}')