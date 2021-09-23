def calculate(k, a, b):
    if k == '+':
        return a + b
    elif k == '-':
        return a - b
    elif k == '*':
        return a * b
    elif k == '/':
        return a / b


def order(k):
    if k <= N:
        if len(tree[k]) > 1:
            order(tree[k][1])
            order(tree[k][2])
        stack.append(tree[k][0])
        if type(tree[k][0]) == str:
            op = stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append(calculate(op, a, b))


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    stack = []

    for _ in range(N):
        temp = list(input().split())
        idx = int(temp.pop(0))
        if len(temp) == 1:
            tree[idx] = list(map(int, temp))
        else:
            tree[idx] = list(temp[0]) + list(map(int, temp[1:]))
    order(1)
    print(f'#{tc} {int(stack[0])}')
