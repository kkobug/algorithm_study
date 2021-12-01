"""
https://www.acmicpc.net/problem/1463
"""
X = int(input())
arr = [0] * (X+1)
for i in range(2, X+1):
    temp = arr[i-1] + 1
    if i % 3 == 0:
        temp = min(temp, arr[i//3] + 1)
    if i % 2 == 0:
        temp = min(temp, arr[i//2] + 1)
    arr[i] = temp

print(arr[-1])