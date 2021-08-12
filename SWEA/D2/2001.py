def flapper():
    for tc in range(1, 1 + int(input())):
        N, K = map(int, input().split())

        NET = [list(map(int, input().split())) for _ in range(N)]

        kill = 0
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                temp = 0
                for k in range(K):
                    for l in range(K):
                        temp += NET[i + k][j + l]

                if temp > kill:
                    kill = temp
        print("#{} {}".format(tc, kill))


flapper()
