def find_pass(ti, tj):
    if city[ti][tj] == 2 and passenger.get((ti, tj)):
        return ti, tj, 0
    Q = [(ti, tj)]
    visited = [[False]*N for _ in range(N)]
    visited[ti][tj] = True
    flag = True
    temp = -1

    while Q:
        i, j = Q.pop(0)
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and city[ni][nj] != 1:
                if flag:  # 승객을 찾으면 append 중단
                    Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

                if city[ni][nj] > 1:  # 승객이네?
                    if flag:  # 찾은 승객이 없네?
                        tempi, tempj = ni, nj
                        temp = visited[ni][nj]  # 사용한 연료
                        flag = False

                    if not flag and temp > visited[ni][nj]:
                        if ni < tempi:
                            tempi, tempj = ni, nj
                        elif ni > tempi:
                            pass
                        else:
                            if nj < tempj:
                                tempi, tempj = ni, nj

    if flag:
        return ti, tj, -1
    return tempi, tempj, temp-1


def find_flag(ti, tj, k):
    Q = [(ti, tj)]
    visited = [[False]*N for _ in range(N)]
    visited[ti][tj] = True

    while Q:
        i, j = Q.pop(0)
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and city[ni][nj] != 1:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

                if (ni, nj) == k:
                    return ni, nj, visited[ni][nj]-1
    return ti, tj, -1


N, M, E = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
taxi, taxj = map(int, input().split())
taxi -= 1
taxj -= 1
passenger = {}
ans = 0
for k in range(M):
    si, sj, ei, ej = map(int, input().split())
    city[si-1][sj-1] = 2
    passenger[(si-1, sj-1)] = (ei-1, ej-1)

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for tc in range(M):
    taxi, taxj, cost1 = find_pass(taxi, taxj)
    city[taxi][taxj] = 0
    print(taxi, taxj, cost1)

    E -= cost1
    # print(E)
    if E < 0 or cost1 == -1:
        ans = -1
        break

    who = passenger[(taxi, taxj)]
    taxi, taxj, cost2 = find_flag(taxi, taxj, who)
    # city[taxi][taxj] = 0
    print(taxi, taxj, cost2)

    E -= cost2
    print(E)
    if E < 0 or cost2 == -1:
        ans = -1
        break

    E += 2 * cost2
    print(E)

if ans == -1: print(ans)
elif E: print(E)
