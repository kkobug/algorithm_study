"""
https://www.acmicpc.net/problem/2042
"""
from sys import stdin
input = stdin.readline


def segmentify(node, st, ed):
    if st == ed:
        tree[node] = nums[st]
        return tree[node]

    mid = (st + ed) // 2
    left = segmentify(node*2, st, mid)
    right = segmentify(node*2+1, mid+1, ed)
    tree[node] = left + right
    return tree[node]


def modify(node, st, ed, idx, value_new):
    if st <= idx <= ed:
        if st == ed:
            tree[node] = value_new
            return

        mid = (st + ed) // 2
        modify(node*2, st, mid, idx, value_new)
        modify(node*2+1, mid+1, ed, idx, value_new)
        tree[node] = tree[node*2] + tree[node*2+1]


def prefix_sum(node, st, ed, value_st, value_ed):
    if value_st > ed or value_ed < st:
        return 0

    if value_st <= st and value_ed >= ed:
        return tree[node]

    mid = (st + ed) // 2
    return prefix_sum(node*2, st, mid, value_st, value_ed) + prefix_sum(node*2+1, mid+1, ed, value_st, value_ed)


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (4*N)
segmentify(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        modify(1, 0, N-1, b-1, c)
    else:
        print(prefix_sum(1, 0, N-1, b-1, c-1))