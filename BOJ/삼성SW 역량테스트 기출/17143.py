"""
https://www.acmicpc.net/problem/17143
"""
R, C, M = map(int, input().split())
ans = 0
sharks = []
for _ in range(M):
    arr = list(map(int, input().split()))
    arr[0] -= 1
    arr[1] -= 1
    sharks.append(arr)
dirs = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, 1),
    4: (0, -1),
}

# 낚시꾼 위치를 반복문으로 돌면서
for king in range(C):
    now_z = 0  # 못잡으면 0
    now_r = R  # 물고기는 바닥부터 체크
    k = -1
    for now in range(M):
        if not sharks[now]:
            continue
        # 좌표, 속력, 방향, 크기
        r, c, s, d, z = sharks[now]
        # 만약, 낚시꾼과 같은 위치에 있고, 땅에 가까운 상어라면 크기 갱신
        if king == c and r < now_r:
            now_z = z
            now_r = r
            k = now
    if -1 < k:
        ans += now_z
        sharks[k] = []

    arr = [[False]*C for _ in range(R)]
    for now in range(M):
        if not sharks[now]:
            continue
        r, c, s, d, z = sharks[now]
        nr = r + s*dirs[d][0]
        nc = c + s*dirs[d][1]
        while not 0 <= nr < R:
            if nr < 0:
                nr *= -1
                sharks[now][3] = 3 - sharks[now][3]
            else:
                nr = 2*(R-1) - nr
                sharks[now][3] = 3 - sharks[now][3]
        while not 0 <= nc < C:
            if nc < 0:
                nc *= -1
                sharks[now][3] = 7 - sharks[now][3]
            else:
                nc = 2*(C-1) - nc
                sharks[now][3] = 7 - sharks[now][3]
        if type(arr[nr][nc]) == int and sharks[arr[nr][nc]][-1] > z:
            sharks[now] = []
        else:
            if type(arr[nr][nc]) == int:
                sharks[arr[nr][nc]] = []
            arr[nr][nc] = now
            sharks[now][0] = nr
            sharks[now][1] = nc
print(ans)