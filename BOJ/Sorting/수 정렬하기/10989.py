"""
https://www.acmicpc.net/problem/10989
"""
import sys
N = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    if arr[i]:
        for _ in range(arr[i]):
            print(i)