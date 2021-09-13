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