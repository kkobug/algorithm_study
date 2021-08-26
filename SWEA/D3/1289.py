for tc in range(1, 1+int(input())):
    memo = input()
    cnt = int(memo[0])

    for i in range(len(memo)-1):
        if memo[i] != memo[i+1]:
            cnt += 1

    print("#{} {}".format(tc, cnt))
