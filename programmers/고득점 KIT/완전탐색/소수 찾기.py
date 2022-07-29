"""
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""
def solution(numbers):
    answer_set = set()
    n = len(numbers)
    N = 10 ** n

    sieve = [False, False] + [True] * N
    for i in range(2, N):
        if i <= N and sieve[i]:
            k = 2
            while i * k <= N:
                sieve[i * k] = False
                k += 1

    check = [False] * n
    result = []

    def get_order():
        nonlocal check, numbers, result, answer_set, sieve
        if 0 < len(result) <= n:
            temp = ""
            for r in result:
                temp += numbers[r]
            temp = int(temp)
            if sieve[temp]:
                answer_set.add(temp)

        if len(result) == n:
            return

        for i in range(n):
            if check[i]:
                continue
            check[i] = True
            result.append(i)
            get_order()
            check[i] = False
            result.pop()

    get_order()
    return len(answer_set)


print(solution("17"))
print(solution("011"))
print(solution("123"))
