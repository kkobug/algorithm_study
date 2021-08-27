def inorder(n):
    if 2*n < N+1:
        inorder(2*n)
    print(tree[n], end="")
    if 2*n + 1 < N+1:
        inorder(2*n + 1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        node = input().split()
        tree[int(node[0])] = node[1]

    print(f"#{tc}", end=" ")
    inorder(1)
    print()
