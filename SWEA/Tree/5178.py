def order(k):
    if k <= N:
        order(2*k)
        order(2*k+1)
        if not tree[k]:
            if 2*k <= N:
                tree[k] += tree[2*k]
            if 2*k+1 <= N:
                tree[k] += tree[2*k+1]

for tc in range(1, 1+int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    order(L)
    print(f'#{tc} {tree[L]}')