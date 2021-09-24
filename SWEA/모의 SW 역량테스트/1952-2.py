for tc in range(1, 1+int(input())):
    D, M, TM, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = min(plan[i-1]*D, M) + dp[i-1]
        if 3 <= i:
            dp[i] = min(dp[i], dp[i-3] + TM)

    if dp[-1] < Y:
        Y = dp[-1]
    print(f'#{tc} {Y}')
