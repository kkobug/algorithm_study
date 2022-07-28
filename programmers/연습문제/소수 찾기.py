"""
https://school.programmers.co.kr/learn/courses/30/lessons/12921
"""
def solution(n):
    sieve = [False] * 2 + [True] * (n-1)
    for i in range(2, n):
        k = 2
        while k * i <= n:
            sieve[k*i] = False
            k += 1
    return sum(sieve)


print(solution(1000000))
print(solution(5))
