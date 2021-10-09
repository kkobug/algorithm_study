def move(i, j, N=''):
    if len(N) == 7:
        ans.add(N)
        return

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            move(ni, nj, N+board[i][j])


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for tc in range(int(input())):
    board = [list(input().split()) for _ in range(4)]
    ans = set()
    for r in range(4):
        for c in range(4):
            move(r, c)
    print(f'#{tc+1} {len(ans)}')