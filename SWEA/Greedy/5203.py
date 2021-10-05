def is_gin(X):
    nums = [0] * 10
    for i in X:
        nums[i] += 1
    i = 0
    while i < 10:
        if nums[i] >= 3:
            return True
        elif i >= 2 and nums[i-2] and nums[i-1] and nums[i]:
            return True
        i += 1
    return False

for tc in range(1, 1+int(input())):
    cards = list(map(int, input().split()))
    A = cards[::2]
    B = cards[1::2]
    ans = 0
    for i in range(3, 7):
        a = is_gin(A[:i])
        b = is_gin(B[:i])
        if a or b:
            if a and b:
                ans = 0
            elif a:
                ans = 1
            else:
                ans = 2
            break
    print(f'#{tc} {ans}')