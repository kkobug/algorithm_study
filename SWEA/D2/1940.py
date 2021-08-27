for tc in range(1, 1+int(input())):
    d = v = 0
    for _ in range(int(input())):
        acc = list(map(int, input().split()))
        if acc[0] == 1:
            v += acc[1]
        elif acc[0] == 2:
            v -= acc[1]
            if v < 0:
                v = 0

        d += v

    print("#{} {}".format(tc, d))
