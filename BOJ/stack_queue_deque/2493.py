"""
https://www.acmicpc.net/problem/2493
"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
top = [0, 0]  # idx, value
ans = []

for i in range(N):
    # 높이가 가장 높은 탑이 나오면
    if top[1] < arr[i]:
        top = [i+1, arr[i]]
        stack = [[i+1, arr[i]]]
        ans.append(0)
        continue

    while stack[-1][1] < arr[i]:
        stack.pop()
    ans.append(stack[-1][0])
    stack.append([i+1, arr[i]])

print(*ans)