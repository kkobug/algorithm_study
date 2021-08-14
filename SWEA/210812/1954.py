def snail():
    """
    달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
    다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

    [예제]
    N이 3일 경우,
    N이 4일 경우,

    [제약사항]
    달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

    [입력]
    가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
    각 테스트 케이스에는 N이 주어진다.

    [출력]
    각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
    (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
    """
    for tc in range(1, 1 + int(input())):
        N = int(input())
        ans = [[0] * N for n in range(N)]
        p = 0
        num = 1

        if N % 2:
            ans[N // 2][N // 2] = N ** 2

        N = N - 1
        while N >= 1:
            for i in range(N):
                ans[p][p + i] = num
                num += 1
            for j in range(N):
                ans[p + j][p + N] = num
                num += 1
            for k in range(N):
                ans[p + N][p + N - k] = num
                num += 1
            for l in range(N):
                ans[p + N - l][p] = num
                num += 1
            p += 1
            N -= 2

        print("#{}".format(tc))
        for t in ans: print(*t)


# snail()


def snail_delta():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for tc in range(1, 1 + int(input())):
        N = int(input())
        ans = [[0] * N for n in range(N)]
        direction = 0
        row = 0
        col = 0
        num = 1

        while num <= N * N:
            ans[row][col] = num
            num += 1

            nr = row + dr[direction]
            nc = col + dc[direction]

            if 0 <= nr < N and 0 <= nc < N and ans[nr][nc] == 0:
                row, col = nr, nc
            else:
                direction = (direction + 1) % 4
                row += dr[direction]
                col += dc[direction]
        print(ans)
    # print("#{}".format(tc))
    # for a in ans: print(*a)


# snail_delta()


def snail_my():
    for tc in range(1, 1 + int(input())):
        N = int(input())
        arr = [[0] * N for _ in range(N)]
        dr = [1, 0, -1, 0]
        dc = [0, -1, 0, 1]
        row, col = 0, N-1
        num, d = 1, 0

        while num <= N * N:
            arr[row][col] = num
            num += 1

            nr, nc = row + dr[d], col + dc[d]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                row, col = nr, nc
            else:
                d = (d+1)%4
                row += dr[d]
                col += dc[d]

        print(tc)
        for i in range(N):
            print(*arr[i])


snail_my()