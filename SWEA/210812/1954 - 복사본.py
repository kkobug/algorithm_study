def snail():
    for tc in range(1, 1 + int(input())):
        N = int(input())
        ans = [[0] * N for n in range(N)]
        p = 0
        num = 1

        if N % 2:
            ans[N // 2][N // 2] = N ** 2

        N = N - 1
        while N >= 1:
            for i in range(N):
                ans[p][p + i] = num
                num += 1
            for j in range(N):
                ans[p + j][p + N] = num
                num += 1
            for k in range(N):
                ans[p + N][p + N - k] = num
                num += 1
            for l in range(N):
                ans[p + N - l][p] = num
                num += 1
            p += 1
            N -= 2

        print("#{}".format(tc))
        for t in ans:
            print(' '.join(map(str, t)))


snail()
