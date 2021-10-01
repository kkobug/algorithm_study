def play(i=0, k=0):
    if k[0] == 2:
        return 1
    elif k[1] == 2:
        return 2

    if nums[i] >= 3:
        nums[i] -= 3
        p[k%2] += 1
        return play(i, k+1)
    elif 2 <= i:



for tc in range(1, 1+int(input())):
    gin = list(map(int, input().split()))
    nums = [0] * 10
    ans = 0
    for g in gin:
        nums[g] += 1
    print(nums)
    i = 0
    turn = 0
    p = [0, 0]