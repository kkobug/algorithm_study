"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""
def make_4(number):
    if len(number) == 1:
        return number * 4
    elif len(number) == 2:
        return number * 2
    elif len(number) == 3:
        return number + number[0]
    else:
        return number


def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: make_4(x), reverse=True))))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
