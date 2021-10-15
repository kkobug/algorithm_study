from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(int(input())):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    ret = [[2048]*N for _ in range(N)]
    ret[0][0] = 0  # 시작점의 비용은 0
    Q = deque([(0, 0)])
    while Q:
        i, j = Q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                cost = max(0, region[ni][nj]-region[i][j]) + 1 + ret[i][j]  # 다음 칸 가는데 드는 비용
                if cost < ret[ni][nj]:  # 다음 칸에 갈 비용이 갱신되어있지 않거나 알고있던 것 보다 비싸면 갱신
                    ret[ni][nj] = cost
                    Q.append((ni, nj))  # 가격이 갱신된 칸 주변도 확인하기 위해 append
    print(f'#{tc+1} {ret[-1][-1]}')
