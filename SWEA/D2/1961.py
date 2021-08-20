def rotate():
    """
    N x N 행렬이 주어질 때,
    시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

    [제약 사항]
    N은 3 이상 7 이하이다.

    [입력]
    가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
    각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
    다음 N 줄에는 N x N 행렬이 주어진다.

    [출력]
    출력의 첫 줄은 '#t'로 시작하고,
    다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
    입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
    (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
    """
    for tc in range(1, 1 + int(input())):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        r_90 = [[0] * N for _90 in range(N)]
        r_180 = [[0] * N for _180 in range(N)]
        r_270 = [[0] * N for _270 in range(N)]

        for i in range(N):
            for j in range(N):
                r_90[j][N - 1 - i] = str(arr[i][j])
                r_180[N - 1 - i][N - 1 - j] = str(arr[i][j])
                r_270[N - 1 - j][i] = str(arr[i][j])

        print("#{}".format(tc))
        for k in range(N):
            print("{} {} {}".format(''.join(r_90[k]), ''.join(r_180[k]), ''.join(r_270[k])))


rotate()


def rotate_90(array, N):
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[j][N-1-i] = array[i][j]

    return ans


for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    r_90 = rotate_90(arr, N)
    r_180 = rotate_90(r_90, N)
    r_270 = rotate_90(r_180, N)
    print("#{}".format(tc))
    for k in range(N):
        print("{} {} {}".format(''.join(r_90[k]), ''.join(r_180[k]), ''.join(r_270[k])))
