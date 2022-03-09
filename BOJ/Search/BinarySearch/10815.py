"""
https://www.acmicpc.net/problem/10815
"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
ans = []

reference = dict()
for i in range(N):
    reference[arr[i]] = arr[i]

for i in range(M):
    if reference.get(nums[i]):
        ans.append("1")
    else:
        ans.append("0")

print(' '.join(ans))