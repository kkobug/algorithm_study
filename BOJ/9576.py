def give(k):
    if visited[k]:
        return
    visited[k] = True
    for j in students[k]:
        if not books[j] or give(books[j]):  # 책을 안줬거나, 앞사람이 다른책 고를수있으면
            books[j] = k
            return 1
    return


for tc in range(int(input())):
    N, M = map(int, input().split())

    students = []
    books = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        students.append([b for b in range(a, b+1)])

    for i in range(M):
        visited = [False] * (N+1)
        give(i)

    ans = 0
    for b in books:
        if b:
            ans += 1

    print(ans)