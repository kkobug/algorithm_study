"""
https://www.acmicpc.net/problem/12886
"""
def stone_group(X, Y, Z):
    total = X+Y+Z
    if total % 3:
        return 0

    visit = [[False]*(total+1) for _ in range(total+1)]
    stack = [(X, Y, Z)]
    while stack:
        x, y, z = stack.pop()
        x_, y_, z_ = x, y, z
        if x == z:
            return 1

        if visit[x][z]:
            continue
        visit[x][z] = True
        
        x_ -= y_
        y_ += y_
        x_, z_ = max(x_, y_, z_), min(x_, y_, z_)
        y_ = total-x_-z_
        stack.append((x_, y_, z_))
        
        x -= z
        z += z
        x, z = max(x, y, z), min(x, y, z)
        y = total-x-z
        stack.append((x, y, z))
    return 0

A, B, C = map(int, input().split())
a, c = max(A, B, C), min(A, B, C)
b = A+B+C-a-c
print(stone_group(a, b, c))
