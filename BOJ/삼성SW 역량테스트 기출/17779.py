"""
https://www.acmicpc.net/problem/17779
예제 입력
6
1 2 3 4 1 6
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9
예제 출력
18
"""
def gerry(r, c, d1, d2):
    try:
        _1 = _2 = _3 = _4 = 0
        for i in range(r):
            for j in range(c+1):
                _1 += city[i][j]
        for d in range(d1):
            for j in range(c-d):
                _1 += city[r+d][j]
        r += d1
        c -= d1
        for i in range(r, N):
            for j in range(c):
                _3 += city[i][j]
        for d in range(d2):
            for i in range(r+d+1, N):
                _3 += city[i][c+d]
        r += d2
        c += d2
        for i in range(r+1, N):
            for j in range(c, N):
                _4 += city[i][j]
        for d in range(d1):
            for j in range(c+d+1, N):
                _4 += city[r-d][j]
        r -= d1
        c += d1
        for i in range(r+1):
            for j in range(c+1, N):
                _2 += city[i][j]
        for d in range(d2):
            for i in range(r-d):
                _2 += city[i][c-d]
        _5 = total - (_1+_2+_3+_4)
        return max(_1, _2, _3, _4, _5) - min(_1, _2, _3, _4, _5)
    except:
        return 2000


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
total = sum(map(sum, city))
ans = 2000
for _r in range(N-2):
    for _c in range(1, N-1):
        for _d1 in range(1, _c+1):
            for _d2 in range(1, N-_c):
                ans = min(ans, gerry(_r, _c, _d1, _d2))
print(ans)