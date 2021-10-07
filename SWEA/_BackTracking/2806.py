def queen(idx=0):
    global ans
    if idx == N:
        ans += 1
        return

    for i in range(N):
        if visit[i]:  # 같은 열 체크
            continue
        flag = True
        for j in range(1, 1+idx):  # 대각선 체크
            if (0 <= i-j < N and board[idx-j][i-j]) or (0 <= i+j < N and board[idx-j][i+j]):
                flag = False
                break
        if flag:
            board[idx][i] = visit[i] = True
            queen(idx+1)
            board[idx][i] = visit[i] = False


for tc in range(int(input())):
    N = int(input())
    board = [[False]*N for _ in range(N)]
    visit = [False]*N
    ans = 0
    queen()
    print(f'#{tc+1} {ans}')