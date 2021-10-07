def size(x):
    global ans
    ans += 1
    if child[x]:
        for i in child[x]:
            size(i)

for tc in range(1, 1+int(input())):
    V, E, A, B = map(int, input().split())
    tree = list(map(int, input().split()))
    child = [[] for _ in range(V+1)]
    parent = [[] for _ in range(V+1)]

    for i in range(0, 2*E, 2):
        child[tree[i]].append(tree[i+1])
        parent[tree[i+1]].append(tree[i])

    pA = parent[A][0]
    pB = parent[B][0]
    while pA != pB:
        if pA < pB:
            pB = parent[pB][0]
        else:
            pA = parent[pA][0]

    ans = 0
    size(pA)
    print(f'#{pA} {ans}')
