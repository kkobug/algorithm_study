def is_road_asc(X):
    st= X[0]
    i = 1
    flag = True
    while i < N:
        if X[i]+1 == st:
            return False
        if X[i] == st:
            i += 1
            continue
        elif flag and X[i]-1 == st:
            if i < L:
                return False
            else:
                flag = False
                st += 1
                i += 1
    return True


def is_road_desc(X):
    st = X[0]
    i = 1
    while i < N:
        if X[i] == st:
            i += 1
        elif X[i]+1 == st:
            k = 0
            while k < L:
                try:
                    if X[i+k]+1 == st:
                        X[i+k] += 1
                        k += 1
                    else:
                        return False
                except:
                    return False
            i = i+k
    return True


def check(X):
    maxX = max(X)
    minX = min(X)
    if maxX == minX: return True
    elif maxX == minX + 1:
        if X[0] == maxX:
            return is_road_desc(X)
        else:
            return is_road_asc(X)
    else: return False


N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    A, B = [], []
    for j in range(N):
        A.append(road[i][j])
        B.append(road[j][i])
    if check(A):
        ans += 1
    if check(B):
        ans += 1
print(ans)