"""
https://www.acmicpc.net/problem/7579
"""
N, M = map(int, input().split())
memory_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))
max_cost = sum(cost_list)
dp = [0] * (max_cost + 1)
ans = max_cost
for i in range(N):
    memory = memory_list[i]
    cost = cost_list[i]

    for j in range(max_cost, cost-1, -1):
        dp[j] = max(dp[j], dp[j-cost] + memory)
        if M <= dp[j] and j < ans:
            ans = j
print(ans)