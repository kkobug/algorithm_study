"""
https://www.acmicpc.net/problem/1637
"""
from sys import stdin
input = stdin.readline

def cnt(k):
    total = 0
    for i in range(N):
        if arr[i][0] <= k:
            total += (min(k, arr[i][1]) - arr[i][0]) // arr[i][2] + 1
    return total

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
left = 1
right = 2147483648
while left < right:
    mid = (left + right) // 2
    total = cnt(mid)
    if total % 2:  # 구간 개수 합이 홀수라면 오른쪽을 당기고
        right = mid
    else:          # 구간 개수 합이 짝수라면 왼쪽을 밀고
        left = mid + 1

if 2147483647 < left:
    print("NOTHING")
else:
    print(left, cnt(left) - cnt(left-1))
