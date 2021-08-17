def isprime(num):
    div = 2
    cnt = 0
    lim = num // 2

    while div <= lim:
        if num % div == 0:
            cnt += 1
            num /= div
        else:
            div += 1

    return cnt


ans = 0
A, B = map(int, input().split())
for i in range(A, B + 1):
    k = isprime(i)
    if k != 0 and isprime(k) == 0:
        ans += 1

print(ans)