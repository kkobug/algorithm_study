def NnM(idx=0):
    if idx == M:
        print(*ans)
        return

    for i in range(N):
        if 0 < i:
            if nums[i-1] == nums[i]:
                continue
        if i == idx:
            continue
        ans.append(nums[i])
        NnM(idx+1)
        ans.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
NnM()
print(ans)