"""
https://www.acmicpc.net/problem/1920
"""
# 단순(이분) 탐색 문제에서, 딕셔너리를 활용하여 쉽게 문제를 해결하기
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
ret = []

reference = dict()
for i in range(N):
    reference[arr[i]] = arr[i]

for i in range(M):
    if reference.get(nums[i]):
        ret.append("1")
    else:
        ret.append("0")

print('\n'.join(ret))