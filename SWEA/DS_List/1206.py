def view():
    for tc in range(1, 11):
        result = 0
        T = int(input()) # == len(build)
        build = list(map(int, input().split()))
        for bld in range(2, T-2):
            block = [build[bld-2], build[bld-1], build[bld+1], build[bld+2]]
            top = block[0]
            for i in block:
                if i > top:
                    top = i
            if build[bld] > top:
                result += (build[bld] - top)

        print("#{} {}".format(tc, result))

view()