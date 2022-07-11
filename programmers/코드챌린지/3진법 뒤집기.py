"""
https://school.programmers.co.kr/learn/courses/30/lessons/68935
"""
def solution(n):
    answer = 0
    third_n = []
    while 0 < n:
        rest = n % 3
        n //= 3
        third_n.append(rest)

    d = 1
    for third in third_n[::-1]:
        answer += third * d
        d *= 3

    return answer


print(solution(45))
print(solution(125))
