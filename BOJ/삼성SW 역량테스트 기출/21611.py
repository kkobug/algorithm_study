"""
https://www.acmicpc.net/problem/21611
"""
from copy import deepcopy
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
ans = 0

# 참조용 숫자판 만들기
nums = [0]*(N*N)
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
_n = d = 0
i = j = N//2
for k in range(2, 2*N+1):
    for _ in range(k//2):
        nums[_n] = (i, j)
        i += di[d]
        j += dj[d]
        _n += 1
    d += 1
    d %= 4

# 구슬판 만들기
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
# M번 마법 시전
for _ in range(M):
    # 블리자드 방향과 거리
    _d, _s = map(int, input().split())
    # 블리자드
    i = j = N//2
    for blizzard in range(_s):
        i += dr[_d]
        j += dc[_d]
        board[i][j] = 0

    # 뿌요뿌요
    flag = True
    while flag:
        flag = False
        bead = 0
        stack = []
        for i, j in nums:
            if not board[i][j]:
                continue
            if board[i][j] == bead:  # 같은 구슬 나오면 추가
                stack.append((i, j))
            else:
                bead = board[i][j]
                if 4 <= len(stack):  # 4개가 안되면 바뀐구슬 하나만 담고 지나가기
                    flag = True
                    while stack:
                        _i, _j = stack.pop()
                        ans += board[_i][_j]
                        board[_i][_j] = 0
                stack = [(i, j)]
    if 4 <= len(stack):
        flag = True
        while stack:
            _i, _j = stack.pop()
            ans += board[_i][_j]
            board[_i][_j] = 0


    # 구슬 바꾸기
    temp_board = [[0]*N for _ in range(N)]
    bead = 0
    cnt = 1
    stack = []
    A = B = 0
    for i, j in nums:
        if not board[i][j]:  # 폭발한 자리면 그냥 무시해
            continue

        if board[i][j] == bead:
            stack.append((i, j))
        else:
            bead = board[i][j]
            if stack:
                A = len(stack)
                B = board[stack[0][0]][stack[0][1]]
            else:
                stack = [(i, j)]
                continue
            for b in (A, B):
                _i, _j = nums[cnt]
                temp_board[_i][_j] = b
                cnt += 1
            if N * N <= cnt: break
            stack = [(i, j)]

    if stack and cnt < N*N:
        A = len(stack)
        B = board[stack[0][0]][stack[0][1]]
        for b in (A, B):
            _i, _j = nums[cnt]
            temp_board[_i][_j] = b
            cnt += 1

    board = deepcopy(temp_board)

print(ans)