for tc in range(1, 11):
    length, nums = input().strip().split()
    PW = []
    for n in nums:
        if PW:
            if PW[-1] == n:
                PW.pop()
            else:
                PW.append(n)
        else:
            PW.append(n)

    print("#{} {}".format(tc, ''.join(PW)))