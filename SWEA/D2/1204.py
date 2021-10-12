for _ in range(int(input())):
    tc = int(input())
    nums = list(map(int, input().split()))
    ans = [0]*101
    for n in nums:
        ans[n] += 1
    idx = 0
    num = 0
    for i in range(100, -1, -1):
        if num < ans[i]:
            num = ans[i]
            idx = i
    print(f'#{tc} {idx}')