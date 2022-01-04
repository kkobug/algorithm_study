"""
https://www.acmicpc.net/problem/15657
예제 입력 2
4 2
9 8 7 1
예제 출력 2
1 1
1 7
1 8
1 9
7 7
7 8
7 9
8 8
8 9
9 9
"""
def NnM(idx=0, j=0):
    if idx == M:
        print(*ans)
        return

    for i in range(j, N):
        ans.append(nums[i])
        NnM(idx+1, i)
        ans.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
NnM()