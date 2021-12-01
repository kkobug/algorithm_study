"""
https://www.acmicpc.net/problem/3015
"""
from sys import stdin
input = stdin.readline

N = int(input())
ans = 0
stack = [int(input())]
for _ in range(N-1):
    num = int(input())
    if num < stack[-1]:
        stack.append(num)
        ans += 1
    elif num >= stack[-1]:
        while stack and num > stack[-1]:
            stack.pop()
            ans += 1

        if stack:
            if stack[0] == num:
                ans += len(stack)
            else:
                idx = -1
                while num == stack[idx]:
                    ans += 1
                    idx -= 1
                ans += 1
        stack.append(num)

print(ans)
