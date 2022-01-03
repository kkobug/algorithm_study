"""
https://www.acmicpc.net/problem/9576
* 정렬 후 greedy solve 가능하나, 이분매칭 연습을 위한 풀이
"""
from sys import stdin
input = stdin.readline


def match(k):
    if visit[k]:
        return
    visit[k] = True
    for j in student[k]:
        if not book[j] or match(book[j]):
            book[j] = k
            return True
    return


for tc in range(int(input())):
    N, M = map(int, input().split())
    book = [0] * (N+1)
    student = [[]]
    for _ in range(M):
        a, b = map(int, input().split())
        student.append([i for i in range(a, b+1)])

    ans = 0
    for i in range(1, 1+M):
        visit = [False] * (M+1)
        if match(i):
            ans += 1

    print(ans)