def cook(p, c):
    fire = c[:N]
    idx = 0
    cheese_idx = N

    while 0 < fire[idx] and 0 < fire[(idx+1)%N]:
        fire[idx] //= 2

        if fire[idx] == 0 and cheese_idx < p:
            fire[idx] = c[cheese_idx]
            cheese_idx += 1

        idx = (idx + 1) % N

    return fire




for tc in range(1, 1+int(input())):
    N, pizza = map(int, input().split())  # 화덕 크기와 피자 개수
    cheese = list(map(int, input().split()))

    print("#{} {}".format(tc, cook(pizza, cheese)))
