def dfs(idx=0, cnt=-1):  # 백트래킹으로 풀 때 사용할 bfs
    global ans
    if ans <= cnt:
        return

    if idx >= N:
        ans = cnt
        return

    k = idx + stop[idx]
    for i in range(idx+1, k+1):
        dfs(i, cnt+1)


for tc in range(int(input())):
    stop = list(map(int, input().split()))
    N = stop.pop(0)

    # DP 코드는 아래 주석을 해제하고 실행
    dp = [-1] * N
    for i in range(N-1):
        for j in range(1, 1+stop[i]):
            if i+j >= N:
                break
            if dp[i+j] == -1:
                dp[i+j] = dp[i] + 1
            else:
                dp[i+j] = min(dp[i]+1, dp[i+j])
    print(f'#{tc+1} {dp[-1]}')

    # backtrcking 코드는 아래 주석을 해제하고 실행
    # N -= 1
    # ans = 100
    # dfs()
    # print(f'#{tc+1} {ans}')
