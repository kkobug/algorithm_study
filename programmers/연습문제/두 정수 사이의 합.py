def solution(a, b):
    if a == b: return a
    elif b < a:
        a, b = b, a
    return (b*(b+1) - a*(a-1)) // 2


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
print(solution(5, -3))
