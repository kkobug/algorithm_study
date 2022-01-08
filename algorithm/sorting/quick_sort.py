"""
병합정렬과 달리 중심이 아니라 기준이 되는 값(pivot)을 설정하여 이를 기준으로 분할한다.
pivot을 기준으로 크기가 작다면 왼쪽, 크다면 오른쪽으로 넘겨 정렬을 진행한다.
분할의 방법에 따라 Hoare partition & Lomuto partition 등의 방법이 있다.
1. divide, merge 나누어 구현하기
2. divide, merge 통합하여 하나로 구현하되, 리스트가 아닌 인덱스를 활용하여 구현하기

* quick sort의 pivot값이 만약 배열 내의 최소(최대)값일 경우에는
파티션의 한쪽으로만 값이 넘겨지므로 selection sort와 다름이 없어진다.
* 따라서 pivot값은 배열의 중앙값일 경우 가장 빠른 정렬이 이루어진다.
"""

nums = [2, 2, 1, 1, 4, 4, 3, 3, 0, 0]
N = len(nums)


# Hoare-partition
def hoare_quick_sort(st, ed):
    if st >= ed:
        return
    P = nums[st]  # HP, 첫 값을 pivot
    L = st + 1
    R = ed
    while L <= R:
        while L <= R and nums[L] < P: L += 1  # 왼쪽이 pivot 보다 작으면 인덱스 >>
        while L <= R and nums[R] >= P: R -= 1  # 오른쪽이 pivot 보다 크면 인덱스 <<
        if L <= R:  # 역전되지 않았다면 바꾸고
            nums[L], nums[R] = nums[R], nums[L]
    nums[st], nums[R] = nums[R], nums[st]  # pivot 자리잡기
    hoare_quick_sort(st, R-1)
    hoare_quick_sort(R+1, ed)


hoare_quick_sort(0, N-1)
print(nums)


# Lomuto-partition