def push(d):
    global ri, rj, bi, bj, flagR, flagB
    lenR = lenB = 0
    nri = ri + di[d]
    nrj = rj + dj[d]
    nbi = bi + di[d]
    nbj = bj + dj[d]

    while board[nri][nrj] != '#':
        ri += di[d]
        rj += dj[d]
        lenR += 1
        if board[ri][rj] == 'O':
            flagR = True
            break
        nri = ri + di[d]
        nrj = rj + dj[d]

    while board[nbi][nbj] != '#':
        bi += di[d]
        bj += dj[d]
        lenB += 1
        if board[bi][bj] == 'O':
            flagB = True
            break
        nbi = bi + di[d]
        nbj = bj + dj[d]

    if (ri, rj) == (bi, bj) and not flagR and not flagB:
        if lenR > lenB:
            ri -= di[d]
            rj -= dj[d]
        else:
            bi -= di[d]
            bj -= dj[d]


def escape(direction, cnt=0):
    global ans, board, ri, rj, bi, bj, flagR, flagB
    if cnt >= ans or cnt > 10:
        return

    if flagB: return

    if flagR:
        ans = cnt
        return

    flagR = flagB = False
    tri, trj, tbi, tbj = ri, rj, bi, bj
    for d in range(4):
        if cnt == 0:
            push(d)
            escape(d, cnt+1)
            flagR = flagB = False
            ri, rj, bi, bj = tri, trj, tbi, tbj
        elif d%2 != direction%2:
            push(d)
            escape(d, cnt+1)
            flagR = flagB = False
            ri, rj, bi, bj = tri, trj, tbi, tbj


di = [1, 0, -1, 0] # 하 우 상 좌
dj = [0, 1, 0, -1]
d = 0
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            board[i][j] = '.'
            bi, bj = i, j
        elif board[i][j] == 'R':
            ri, rj = i, j
            board[i][j] = '.'

flagR = flagB = False
ans = 11
escape(d)
if ans == 11:
    ans = -1
print(ans)