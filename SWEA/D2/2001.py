def kill_fly():
    for tc in range(int(input())):
        NK = list(map(int, input().split()))

        # 파리 사각형 만들기
        NET = []
        for N in range(NK[0]):
            NET.append(list(map(int, input().split())))

        # 파리지옥
        kill = 0
        for i in range(NK[0] - NK[1] + 1):
            for j in range(NK[0] - NK[1] + 1):
                temp = 0
                for k in range(NK[1]):
                    for l in range(NK[1]):
                        temp += NET[i + k][j + l]

                if temp > kill:
                    kill = temp

        print("#{} {}".format(tc + 1, kill))


kill_fly()
