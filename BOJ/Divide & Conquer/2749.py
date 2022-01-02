"""
https://www.acmicpc.net/problem/2749
"""
N = int(input())
check = {0: 1, 1: 1, 2: 2, 3: 3}
mod = 1000000

def fib(k):
    if k < 4:
        return check[k]

    if k % 2:
        if check.get(k):
            return check[k]
        else:
            n = (k + 1) // 2
            left = fib(n) ** 2
            right = fib(n-2) ** 2
            check[k] = (left - right) % mod
            return check[k]

    else:
        if check.get(k):
            return check[k]
        else:
            n = k // 2
            left = fib(n) ** 2
            right = fib(n-1) ** 2
            check[k] = (left + right) % mod
            return check[k]

print(fib(N-1))
