"""
https://www.acmicpc.net/problem/15663
예제 입력 2
4 2
9 7 9 1
예제 출력 2
1 7
1 9
7 1
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
        if not (visited[i] or last == nums[i]):
            visited[i] = True
            ans.append(nums[i])
            last = nums[i]
            NnM(idx+1)
            visited[i] = False
            ans.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
ans = []
NnM()
