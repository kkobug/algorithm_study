def quick_sort(st, ed):
    if st >= ed:
        return
    P = nums[st]  # HP, 첫 값을 pivot
    L = st + 1
    R = ed
    while L <= R:
        while L <= R and nums[L] <= P: L += 1  # 왼쪽이 pivot 보다 작으면 인덱스 >>
        while L <= R and nums[R] >= P: R -= 1  # 오른쪽이 pivot 보다 크면 인덱스 <<
        if L <= R:  # 역전되지 않았다면 바꾸고
            nums[L], nums[R] = nums[R], nums[L]
    nums[st], nums[R] = nums[R], nums[st]  # pivot 자리잡기
    quick_sort(st, R-1)
    quick_sort(R+1, ed)


for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc+1} {nums[N//2]}')
