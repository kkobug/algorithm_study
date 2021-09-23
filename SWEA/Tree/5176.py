def inorder(k=1):
    global cnt
    if k <= N:
        inorder(2*k)
        tree[k] = cnt
        cnt += 1
        inorder(2*k+1)


for tc in range(1, 1+int(input())):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder()
    print(f"#{tc} {tree[1]} {tree[N//2]}")