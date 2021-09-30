def gerry(x, y, d1, d2):
    a, b, c, d, e = 0, 0, 0, 0, 0
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if i+j < x+y:
                a += city[i][j]

    for i in range(1, x+d2+1):
        for j in range(y+1, N+1):
            if j-i > y-x:
                b += city[i][j]

    for i in range(x+d1+1, N+1):
        for j in range(1, y-d1+d2):
            if i-j > x-y+2*d1:
                c += city[i][j]

    for i in range(x+d2+1, N+1):
        for j in range(y-d1+d2, N+1):
            if i+j > x+y:
                d += city[i][j]

    e = ppl - (a+b+c+d)

    return max(a, b, c, d, e) - min(a, b, c, d, e)


N = int(input())
city = [[0]*(N+1)]
for _ in range(N):
    city.append([0] + list(map(int, input().split())))
ppl = sum(map(sum, city))
ans = 400000
for _r in range(1, N-1):
    for _c in range(2, N-1):
        for _d1 in range(1, N):
            for _d2 in range(1, N):
                if _r+_d1+_d2 <= N and 1 <= _c-_d1 < _c < _c+_d2 <= N:
                    ans = min(ans, gerry(_r, _c, _d1, _d2))

print(ans)



"""
def gerry(x, y, d1, d2):
    a, b, c, d, e = 0, 0, 0, 0, 0
    for i in range(x+d1):
        for j in range(y+1):
            if i+j < x+y:
                a += city[i][j]

    for i in range(x+d2+1):
        for j in range(y+1, N):
            if j-i > y-x:
                b += city[i][j]

    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if i-j > x-y+2*d1:
                c += city[i][j]

    for i in range(x+d2+1, N):
        for j in range(y-d1+d2, N):
            if i+j > x+y:
                d += city[i][j]

    e = ppl - (a+b+c+d)

    return max(a, b, c, d, e) - min(a, b, c, d, e)


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
ppl = sum(map(sum, city))
ans = 400000
for _r in range(N-2):
    for _c in range(1, N-1):
        for _d1 in range(1, N-1):
            for _d2 in range(1, N-1):
                if _d1 <= _c < N-_d2 and _r+_d1+_d2 < N:
                    ans = min(ans, gerry(_r, _c, _d1, _d2))

print(ans)
"""