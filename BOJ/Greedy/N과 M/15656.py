"""
https://www.acmicpc.net/problem/15656
예제 입력 2
4 2
9 8 7 1
예제 출력 2
1 1
1 7
1 8
1 9
7 1
7 7
7 8
7 9
8 1
8 7
8 8
8 9
9 1
9 7
9 8
9 9
"""
def NnM(idx=0):
    global ans
    if idx == M:
        print(*ans)
        return

    for i in range(N):
        ans.append(nums[i])
        NnM(idx+1)
        ans.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
NnM()