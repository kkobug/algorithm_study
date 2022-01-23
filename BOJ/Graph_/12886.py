"""
https://www.acmicpc.net/problem/12886
"""
from collections import deque

def stone_group(X, Y, Z):
    total = X+Y+Z
    if total % 3:
        return 0

    visit = [[False]*(total+1) for _ in range(total+1)]
    Q = deque()
    Q.append((X, Y, Z))
    while Q:
        x, y, z = Q.popleft()
        x_, y_, z_ = x, y, z
        if x == y == z:
            return 1

        if visit[x][z]:
            continue
        visit[x][z] = True
        
        x_ -= y_
        y_ += y_
        x_, z_ = max(x_, y_, z_), min(x_, y_, z_)
        y_ = total-x_-z_
        Q.append((x_, y_, z_))
        
        x -= z
        z += z
        x, z = max(x, y, z), min(x, y, z)
        y = total-x-z
        Q.append((x, y, z))
    return 0

A, B, C = map(int, input().split())
a, c = max(A, B, C), min(A, B, C)
b = A+B+C-a-c
print(stone_group(a, b, c))
