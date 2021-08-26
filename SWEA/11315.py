def omok(i, j, cnt=0):
    global ans

    if cnt >= 5:
        ans = "YES"
        return

    for i in range(N):
        for j in range(N):
            if 0 <= i < N and 0 <= j < N:
                if board[i][j] ==  '.':
                    if j == N-1:
                        omok(i+1, 0, cnt)
                    else:
                        omok(i, j+1, cnt)
                elif board[i][j] == 'o':
                    cnt += 1


for tc in range(1, 1+int(input())):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = "NO"
    omok(0, 0)
    print("#{} {}".format(tc, ans))
