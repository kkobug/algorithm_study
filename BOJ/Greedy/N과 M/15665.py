"""
https://www.acmicpc.net/problem/15665
예제 입력 2
4 2
9 7 9 1
예제 출력 2
1 1
1 7
1 9
7 1
7 7
7 9
9 1
9 7
9 9
"""
def NnM(idx=0):
    if idx == M:
        print(*ans)
        return

    last = 0
    for i in range(N):
        if last != nums[i]:
            last = nums[i]
            ans.append(nums[i])
            NnM(idx+1)
            ans.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
NnM()
