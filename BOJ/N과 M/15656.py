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