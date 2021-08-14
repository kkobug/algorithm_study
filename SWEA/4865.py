def how_many():
    for tc in range(1, 1+int(input())):
        str1 = input()
        str2 = input()
        most = 0
        for s1 in str1:
            cnt = 0
            for s2 in str2:
                if s1 == s2:
                    cnt += 1
            if most < cnt:
                most = cnt
        print("#{} {}".format(tc, most))


how_many()