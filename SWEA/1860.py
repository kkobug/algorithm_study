for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    ppl = sorted(list(map(int, input().split())))
    sale = [0] * (max(ppl)+1)
    eat = fish = 0
    ans = "Possible"
    for i in range(1, max(ppl)+1):
        if (i)%M == 0: fish += K
        if i in ppl: eat += 1
        sale[i] = fish - eat
        if sale[i] < 0: ans = "Impossible"
    print("#{} {}".format(tc, ans))
