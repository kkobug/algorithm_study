"""
https://www.acmicpc.net/problem/2096
https://www.acmicpc.net/problem/15645
"""
from sys import stdin
input = stdin.readline
N = int(input())

max_dp = [0]*3
min_dp = [0]*3
max_now = [0]*3
min_now = [0]*3

for i in range(N):
    now = list(map(int, input().split()))
    for j in range(3):
        maxi = now[j] + max_dp[j]
        mini = now[j] + min_dp[j]
        for k in (-1, 1):
            nj = j+k
            if 0 <= nj < 3:
                maxi = max(maxi, now[j] + max_dp[nj])
                mini = min(mini, now[j] + min_dp[nj])
        max_now[j] = maxi
        min_now[j] = mini
    for k in range(3):
        max_dp[k] = max_now[k]
        min_dp[k] = min_now[k]
print(max(max_dp), min(min_dp))