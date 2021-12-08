"""
https://www.acmicpc.net/problem/11401
"""
def power(x, y):
    if y == 0:
        return 1
    if y % 2:
        return ((power(x, y//2) ** 2) * x) % div
    else:
        return (power(x, y // 2) ** 2) % div


N, K = map(int, input().split())
div = 1000000007
memo = [1] * (N+1)
for i in range(2, N+1):
    memo[i] = memo[i-1]*i % div

num = memo[N]
denom = power(memo[N-K] * memo[K], div-2)

print(num * denom % div)
