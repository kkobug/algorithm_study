"""
* 대각선 방향으로 탐색하며
1. 중복이 있을 경우 가지치기
2. 범위를 벗어나면 가지치기
3. 대각선이 마름모를 이루지 않으면(즉, 1 <= d1 and 1 <= d2) 가지치기

유사문제 : 게리맨더링
"""
def tour(i, j, d1, d2, C):
    r, c = i, j
    try:
        for d in range(1, 1+d1):
            r += 1
            c -= 1
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d2):
            r += 1
            c += 1
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d1):
            r -= 1
            c += 1
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d2):
            r -= 1
            c -= 1
            if (r, c) == (i, j):
                return len(C)
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
    except:
        return -1
    return len(C)


for tc in range(int(input())):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for r in range(N-2):
        for c in range(1, N-1):
            for _d1 in range(1, 1+c):
                for _d2 in range(1, N-c):
                    temp = tour(r, c, _d1, _d2, [cafe[r][c]])
                    ans = max(ans, temp)
    print(f'#{tc+1} {ans}')
