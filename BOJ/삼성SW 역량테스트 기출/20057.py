"""
https://www.acmicpc.net/problem/20057

예제 입력 1
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0
예제 출력 1
10
"""
from sys import stdin as st


def side_check(si, sj, k):
    global ans
    magic[ni][nj] -= total * 7 // 100
    magic[ni][nj] -= total // 100
    if 0 <= si < N and 0 <= sj < N:
        magic[si][sj] += total * 7 // 100
        magic[i + di[(d + k) % 4]][j + dj[(d + k) % 4]] += total // 100

        magic[ni][nj] -= total * 2 // 100
        if 0 <= si + di[(d + k) % 4] < N and 0 <= sj + dj[(d + k) % 4] < N:
            magic[si + di[(d + k) % 4]][sj + dj[(d + k) % 4]] += total * 2 // 100
        else:
            ans += total * 2 // 100

        magic[ni][nj] -= total // 10
        if 0 <= si + di[d] < N and 0 <= sj + dj[d] < N:
            magic[si + di[d]][sj + dj[d]] += total // 10
        else:
            ans += total // 10
    else:
        magic[ni][nj] -= (total // 10 + total // 50)
        ans += (total // 10 + total * 7 // 100 + total // 100 + total // 50)


N = int(st.readline())
magic = [list(map(int, st.readline().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
ans = 0
d = 0
i = j = N // 2
for x in range(2, 2 * N + 1):
    x //= 2
    for y in range(x):
        if i == 0 and j == 0: break
        ni = i + di[d]
        nj = j + dj[d]
        total = magic[ni][nj]

        # 오른쪽 체크
        ri = ni + di[(d - 1) % 4]
        rj = nj + dj[(d - 1) % 4]
        side_check(ri, rj, -1)

        # 왼쪽 체크
        li = ni + di[(d + 1) % 4]
        lj = nj + dj[(d + 1) % 4]
        side_check(li, lj, 1)

        # 앞체크
        if 0 <= ni + di[d] < N and 0 <= nj + dj[d] < N:
            magic[ni][nj] -= total * 5 // 100
            if 0 <= ni + 2 * di[d] < N and 0 <= nj + 2 * dj[d] < N:
                magic[ni + 2 * di[d]][nj + 2 * dj[d]] += total * 5 // 100
            else:
                ans += total * 5 // 100

            magic[ni + di[d]][nj + dj[d]] += magic[ni][nj]
        else:
            ans += magic[ni][nj]
        magic[ni][nj] = 0

        i = ni
        j = nj
    d = (d + 1) % 4
print(ans)
