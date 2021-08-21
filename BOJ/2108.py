def rnd(x):
    if x < 0:
        return -1 * rnd(-x)
    if x % 1 < 0.5:
        return int(x)
    else:
        return int(x+1)


N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

# 산술평균
print(rnd(sum(nums) / N))

# 중앙값
# 선택정렬
print(sorted(nums)[N // 2])

# 최빈값
counting = [0] * 8001
for j in nums:
    counting[j + 4000] += 1

check = max(counting)
mode = 0
cnt = 0
for k in range(8001):
    if check == counting[k]:
        mode = k - 4000
        if cnt == 1:
            break
        cnt += 1
print(mode)

# 범위
print(max(nums) - min(nums))
