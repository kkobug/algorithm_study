def find_set(x):
    if P[x] != x:
        P[x] = find_set(P[x])
    return P[x]

for tc in range(int(input())):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(reverse=True, key=lambda x: x[2])  # sort for KRUSKAL
    P = list(range(V+1))  # make_set
    ans = cnt = 0
    while cnt < V:
        st, ed, w = edges.pop()
        if find_set(st) == find_set(ed):
            continue
        P[find_set(ed)] = find_set(st)  # union
        ans += w
        cnt += 1
    print(f'#{tc+1} {ans}')


# for tc in range(int(input())):
#     V, E = map(int, input().split())
#     tree = [[] for _ in range(V+1)]
#     visit = [True] + [False]*V
#     ans = 0
#     for _ in range(E):
#         st, ed, w = map(int, input().split())
#         tree[st].append([ed, w])
#         tree[ed].append([st, w])
#
#     st = 0
#     while sum(visit) != len(visit):
#         ed = w = 10
#         for i in tree[st]:
#             if i[1] < w and not visit[i[0]]:
#                 ed, w = i
#         visit[ed] = True
#         ans += w
#         st = ed
#     print(ans)