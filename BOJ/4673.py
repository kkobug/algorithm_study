def sum_digit(x):
    s = 0

    while x > 0:
        s += (x % 10)
        x //= 10

    return s


ans = list(range(10001))

for i in range(10001):
    temp = i + sum_digit(i)
    if temp > 10000: continue

    ans[temp] = 0

for j in ans:
    if j: print(j)
