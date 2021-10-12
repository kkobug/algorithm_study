"""
입력과 같은 형태의 벽돌이 있을 때, 각 번호에 따라 벽돌이 폭파
1은 1칸
2는 5칸(+)
3은 9칸(+)
...
N번 구슬을 떨어트려 맨 위의 벽돌을 폭파할 수 있을 때, 최대한 많은 벽돌을 깬 후 남은 벽둘 개수?

1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1


#1 12
"""
from copy import deepcopy as dc
def choice(idx, B, total=0):
    global ans
    ans = max(ans, total)
    if idx == N or ans == st_cnt:
        return

    temp = dc(B)
    for c in range(W):  # 구슬 놓기
        if not B[-1][c]:  # 바닥에 벽돌이 없다면, 그 줄은 넘어감
            continue

        for r in range(H):  # 시작벽돌 고르기
            if B[r][c]:  # 위에서부터 내려오면서, 처음 벽돌 나오는 위치 찾기
                break

        cnt = 0  # 이번 회차에 깬 벽돌 수
        S = [(r, c)]  # 시작 벽돌
        V = [[False]*W for _ in range(H)]
        V[r][c] = True
        while S:  # 벽돌 깨기
            i, j = S.pop()
            if B[i][j] == 1:  # 벽돌이 1이면 그냥 깨고 지나가기
                B[i][j] = 0
                cnt += 1
            elif 1 < B[i][j]:  # 1보다 크면 십자 깨기
                for k in range(1, B[i][j]):
                    for d in range(4):
                        ni = i + k * di[d]
                        nj = j + k * dj[d]

                        if 0 <= ni < H and 0 <= nj < W and B[ni][nj] and not V[ni][nj]:
                            S.append((ni, nj))
                            V[ni][nj] = True
                B[i][j] = 0
                cnt += 1

        for j in range(W):  # 빈칸 메우기
            for i in range(H-1, -1, -1):  # 아래 행부터 올라오면서
                if not B[i][j]:  # 0에서 멈춰!
                    break
            p = i  # i는 0인덱스, p는 벽돌 인덱스
            while 0 <= p:
                if B[p][j]:  # 벽돌이 있는 위치라면
                    B[p][j], B[i][j] = B[i][j], B[p][j]  # 빈칸이랑 자리바꾸고
                    i -= 1  # 0인덱스를 하나 옮기기
                p -= 1
        choice(idx+1, B, total+cnt)
        B = dc(temp)



di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(int(input())):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    st_cnt = 0
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                st_cnt += 1
    choice(0, bricks)
    print(f'#{tc+1} {st_cnt-ans}')
