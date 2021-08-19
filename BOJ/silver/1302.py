N = int(input())
books = {}  # 책장
for i in range(N):
    book = input()
    if book in books:  # 있으면 카운트
        books[book] += 1
    else:  # 없으면 책장에 꽂기
        books[book] = 1

best = 0
for k, v in books.items():
    if v > best:  # 많이팔렸나?
        best = v
        ans = k
    elif v == best:  # 사전순
        if ans > k:
            ans = k

print(ans)