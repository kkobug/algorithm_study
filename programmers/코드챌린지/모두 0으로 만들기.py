"""
https://school.programmers.co.kr/learn/courses/30/lessons/76503
"""
import sys
sys.setrecursionlimit(1000000)


def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    N = len(a)
    tree = []
    visit = []
    for _ in range(N):
        tree.append([])
        visit.append(False)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(k):
        nonlocal answer
        visit[k] = True

        for next_node in tree[k]:
            if visit[next_node]:
                continue
            a[k] += dfs(next_node)
            answer += a[next_node] if a[next_node] > 0 else -a[next_node]

        return a[k]

    dfs(0)
    return answer


print(solution(
    [-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]
))
print(solution(
    [0, 1, 0], [[0, 1], [1, 2]]
))
