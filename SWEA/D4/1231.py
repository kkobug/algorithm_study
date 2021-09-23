def inorder(k):
    if k <= N:
        inorder(2*k)
        print(tree[k], end="")
        inorder(2*k+1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        word = list(input().split())
        tree[int(word[0])] = word[1]
    print(f"#{tc}", end=" ")
    inorder(1)
    print()