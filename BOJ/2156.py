def drink(i=0):
    global ans, temp

    if i == N:
        if ans < temp:
            ans = temp
        return

    if i < 2 or (not check[i-2] or not check[i-1]):
        check[i] = True
        temp += nums[i]
        drink(i+1)
        check[i] = False
        temp -= nums[i]


N = int(input())

nums = [int(input()) for _ in range(N)]
check = [False] * N
ans = temp = 0
drink()
print(ans)