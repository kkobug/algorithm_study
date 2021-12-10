"""
https://www.acmicpc.net/problem/10942
"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
is_palindrome = [[0]*N for _ in range(N)]
for i in range(N-1, -1, -1):
    for j in range(i, N):
        if i == j:
            is_palindrome[i][j] = 1
        elif arr[i] == arr[j]:
            if i+1 == j:
                is_palindrome[i][j] = 1
            elif is_palindrome[i+1][j-1]:
                is_palindrome[i][j] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(is_palindrome[S-1][E-1])
