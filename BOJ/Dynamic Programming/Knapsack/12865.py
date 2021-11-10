"""
https://www.acmicpc.net/problem/12865
"""
# N, K = map(int, input().split())
# dp = [[0]*(K+1) for _ in range(N)]
# W, V = map(int, input().split())
# for j in range(W, K+1):
#     dp[0][j] = V
# for i in range(1, N):
#     W, V = map(int, input().split())
#     if K < W:
#         for j in range(K+1):
#             dp[i][j] = dp[i-1][j]
#     else:
#         for j in range(W):
#             dp[i][j] = dp[i-1][j]
#         for j in range(W, K+1):
#             dp[i][j] = max(dp[i-1][j-W] + V, dp[i-1][j])
#
# print(dp[-1][-1])


N, K = map(int, input().split())
dp = [0] * (K+1)
for i in range(N):
    W, V = map(int, input().split())
    for j in range(K, W-1, -1):
        dp[j] = max(dp[j], dp[j-W]+V)

print(dp[-1])