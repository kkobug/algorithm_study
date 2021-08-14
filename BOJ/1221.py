def water():
    N, K = map(int, input().split())
    x = 0
    while True:
        D = (K + x) / N
        while D % 2 == 0:
            D = D / 2
            if D == 1:
                break
        x += 1
        if D == 1:
            break
    print(x)


water()