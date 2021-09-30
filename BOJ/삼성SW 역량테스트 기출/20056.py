"""
https://www.acmicpc.net/problem/20056
예제 입력
4 2 1
1 1 5 2 2
1 4 7 1 6
예제 출력
8
"""
from copy import deepcopy

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
ground = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    f = list(map(int, input().split()))
    ground[f[0]-1][f[1]-1].append(f[2:])

for __ in range(K):
    n_ground = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = []
            while ground[i][j]:
                temp.append(ground[i][j].pop())

            while temp:
                m, s, d = temp.pop()
                r = (i + s*di[d]) % N
                c = (j + s*dj[d]) % N
                n_ground[r][c].append([m, s, d])


    for i in range(N):
        for j in range(N):
            if 1 < len(n_ground[i][j]):
                temp = []
                while n_ground[i][j]:
                    temp.append(n_ground[i][j].pop())

                m, s, d = 0, 0, []
                for _ in range(len(temp)):
                    m += temp[_][0]
                    s += temp[_][1]
                    if temp[_][2] % 2:
                        d.append(1)
                    else:
                        d.append(0)
                m //= 5
                if not m:
                    continue
                s //= len(temp)
                if sum(d) == 0 or sum(d) == len(temp):
                    d = 0
                else:
                    d = 1

                for _d in range(d, 8, 2):
                    # ni = (i + s*di[_d]) % N
                    # nj = (j + s*dj[_d]) % N
                    n_ground[i][j].append([m, s, _d])

    ground = deepcopy(n_ground)

ans = 0
for i in range(N):
    for j in range(N):
        for k in ground[i][j]:
            ans += k[0]
print(ans)