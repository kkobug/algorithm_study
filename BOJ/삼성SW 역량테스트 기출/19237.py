"""
https://www.acmicpc.net/problem/19237
"""
import sys
input = sys.stdin.readline

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
N, M, K = map(int, input().split())
alive = [False] + [True]*M  # 살아있는 상어 체크
sharks = [[] for _ in range(M+1)]  # 상어 좌표, 방향
smell = [[[] for _ in range(N)] for _ in range(N)]  # 냄새 위치, 남은 시간
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            smell[i][j] = [temp[j], K]
            sharks[temp[j]] = ([i,  j])
temp = list(map(int, input().split()))
for i in range(M):
    sharks[i+1].append(temp[i])
directions = {}
for i in range(1, 1+M):
    temp = [list(map(int, input().split())) for _ in range(4)]
    directions[i] = temp

ans = 0
while ans < 1000:
    ans += 1
    # 이동하기
    for k in range(1, M+1):  # k번째 상어 이동하기
        if not alive[k]:  # 죽었으면 다음 상어 선택
            continue
        i, j, now_d = sharks[k]  # 이번에 이동할 (k번째) 상어의 현재 위치와 방향

        """
        우선순위
        1. 빈칸
        2. k번 상어가 남긴 냄새가 있는 공간
        """
        for d in directions[k][now_d-1]:  # 갱신을 위해 우선순위 순으로 검사
            ni = i + di[d]  # 주변검사를 하면서
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if not smell[ni][nj]:
                    break
        else:
            for d in directions[k][now_d - 1]:  # 갱신을 위해 우선순위 순으로 검사
                ni = i + di[d]  # 주변검사를 하면서
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if smell[ni][nj][0] == k:
                        break
        sharks[k] = [ni, nj, d]

    # 이동하면서 시간 지났음
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = []

    # 냄새 남기거나 쫓겨나기
    visit = [[False]*N for _ in range(N)]
    for k in range(1, M+1):
        if not alive[k]:
            continue
        i, j, d = sharks[k]
        if visit[i][j]:  # 상어가 들어가있으면 숫자 큰 상어는 쫓겨남
            alive[k] = False
            sharks[k] = []
        else:            # 빈자리면 상어가 들어갈 수 있음
            visit[i][j] = True
            smell[i][j] = [k, K]
    if sum(alive) == 1:
        break
else:
    ans = -1

print(ans)
