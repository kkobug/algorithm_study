"""
https://www.acmicpc.net/problem/17404
"""
from sys import stdin
input = stdin.readline


def dp(arr):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])


N = int(input())
red_arr = [[1000001]*3]
green_arr = [[1000001]*3]
blue_arr = [[1000001]*3]
red_arr[0][0], green_arr[0][1], blue_arr[0][2] = list(map(int, input().split()))

for i in range(1, N):
    temp = list(map(int, input().split()))
    red_arr.append(temp[:])
    green_arr.append(temp[:])
    blue_arr.append(temp[:])

    dp(red_arr)
    dp(green_arr)
    dp(blue_arr)

print(min(red_arr[-1][1], red_arr[-1][2], green_arr[-1][0], green_arr[-1][2], blue_arr[-1][0], blue_arr[-1][1]))