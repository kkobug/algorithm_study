def quick_sort(a, start, end):
    if start < end:
        # pivot 고정
        p = partition(a, start, end)
        # pivot 좌 우에 대해 2번 정렬
        quick_sort(a, start, p-1)
        quick_sort(a, start, p+1)


# 호어파티션, 로무토 파티션
def partition(a, start, end):
    pivot = (start + end) // 2
    left = start
    right = end

    while start < right:
        # 왼쪽에 pivot 보다 크거나 같은애가 있으면 선택 (없으면 pivot 선택)
        while (left < right and a[left] < a[pivot]): left += 1
        # 오른쪽에 pivot 보다 작은애가 있으면 선택
        while (left < right and a[right] >= a[pivot]): right -= 1

        # 고른 두 애들 크기가 오른쪽이 더 크면
        if left < right:
            # 오른쪽을 pivot으로 만들어서
            if left == pivot: pivot = right
            # 좌우 교환
            a[left], a[right] = a[right], a[left]

    # 아니면 그냥 교환
    a[pivot], a[right] = a[right], a[pivot]

    # pivot 반환
    return right