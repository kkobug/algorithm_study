for tc in range(int(input())):
    W, N = map(int, input().split())
    trash = [list(map(int, input().split())) for _ in range(N)]
    temp = 0
    dist_temp = 0
    dist = 0

    for i in range(N):
        if temp + trash[i][0] < W:
            temp += trash[i][0]
            dist += trash[i][1]
            dist_temp += trash[i][1]
            continue
