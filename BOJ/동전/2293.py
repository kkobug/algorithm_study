N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

ans = [1] + [0]*K
for i in range(N):
    for k in range(i, K+1):
        ans[k] += ans[k-i]

print(ans)