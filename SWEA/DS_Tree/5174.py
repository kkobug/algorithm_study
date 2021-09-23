def subtree(k):
    global ans
    for i in tree[k]:
        ans += 1
        subtree(i)


for tc in range(1, 1 + int(input())):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    node = list(map(int, input().split()))

    for e in range(E):
        tree[node[e*2]].append(node[e*2 + 1])
    ans = 1
    subtree(N)
    print(f'#{tc} {ans}')
