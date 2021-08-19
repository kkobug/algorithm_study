books = {}
for _ in range(int(input())):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

best = 0
target = '~'
for key, val in books.items():
    if val > best:
        best = val
        target = key
    elif val == best:
        if target[0] > key[0]:
