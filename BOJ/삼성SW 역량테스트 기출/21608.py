"""
https://www.acmicpc.net/problem/21608
조건분기 정리
1. 인접에 좋아하는 사람이 많을수록 (좋아하는 사람이 앉아있는지, 없는지)
2. 좋아하는 사람 수가 같으면 공백이 많을수록 (공백 개수)
3. 행과 열이 가장 작은지
"""
from sys import stdin
input = stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
students = [list(map(int, input().split())) for _ in range(N*N)]
school = [[0]*N for _ in range(N)]  # 각 칸에 몇 번 학생이 있는가
positions = [0]*(N*N+1)  # 몇 번 학생이 어디에 있는가

# 첫 번째 학생의 위치는 고정
school[1][1] = students[0][0]
positions[students[0][0]] = (1, 1)

for now in students[1:]:
    possibility = {}  # n번째 학생의 선호도 조사
    for i in range(1, 5):
        if positions[now[i]]:  # 선호하는 학생이 앉아있다면
            r, c = positions[now[i]]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:  # 범위 안에 있어야해
                    if not school[nr][nc]:  # 거기가 빈자리여야해
                        if possibility.get((nr, nc)):  # 인접 칸이 선호칸에 이미 들어있으면 카운트+1
                            possibility[(nr, nc)] += 1
                        else:                          # 인접 칸이 선호칸에 없으면 하나 만들어주기
                            possibility[(nr, nc)] = 1

    best_possibility = (N-1, N-1)
    pref = blank = -1
    if possibility:
        for k, v in possibility.items():
            if pref == v:  # 좋아하는 사람 수가 같으면
                i, j = k  # 공백검사
                temp_blank = 0
                for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < N and 0 <= nj < N and not school[ni][nj]:
                        temp_blank += 1
                if blank < temp_blank:  # 공백이 더 많으면 갱신
                    blank = temp_blank
                    best_possibility = k
                elif blank == temp_blank:  # 공백이 같으면 좌표검사
                    if best_possibility[0] > k[0]:  # 행이 작다면 무조건 갱신
                        best_possibility = k
                    elif best_possibility[0] == k[0]:  # 행이 같다면
                        if best_possibility[1] > k[1]:  # 열이 작은 좌표로 갱신
                            best_possibilit = k

            elif pref < v:
                best_possibility = k
                pref = v
                i, j = k
                blank = 0
                for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < N and 0 <= nj < N and not school[ni][nj]:
                        blank += 1

            if pref == 4:
                break
    else:  # 선호하는 학생이 아직 없다면
        for i in range(N):
            for j in range(N):
                if school[i][j]:
                    continue
                temp_blank = 0
                for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < N and 0 <= nj < N and not school[ni][nj]:
                        temp_blank +=1

                if blank < temp_blank:
                    best_possibility = (i, j)
                    blank = temp_blank
                if blank == 4:
                    break
            if blank == 4:
                break
    school[best_possibility[0]][best_possibility[1]] = now[0]
    positions[now[0]] = best_possibility

ans = 0
for s in students:
    i, j = positions[s[0]]  # 검사할학생의 위치
    cnt = 0
    for d in range(4):
        ni = i + dr[d]
        nj = j + dc[d]
        if 0 <= ni < N and 0 <= nj < N:
            if school[ni][nj] in s[1:]:
                cnt += 1
    if cnt:
        ans += 10**(cnt-1)

print(ans)
