def child(x):
    global cnt
    cnt += 1
    if tree[x]:
        for i in tree[x]:
            child(i)
    else:
        return
for tc in range(int(input())):
    V, E, A, B = map(int, input().split())
    tree = [[] for _ in range(V+1)]
    parents = [0] * (V+1)
    nums = list(map(int, input().split()))
    for i in range(E):
        tree[nums[2*i]].append(nums[2*i+1])
        parents[nums[2*i+1]] = nums[2*i]

    P = []
    while A:
        P.append(A)
        A = parents[A]
    while B not in P:
        B = parents[B]
    cnt = 0
    child(B)
    print(f'#{1+tc} {B} {cnt}')
