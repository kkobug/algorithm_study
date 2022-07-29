"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""
def number_to_binary(number):
    ret = ""
    while number:
        if number % 2:
            ret = "1" + ret
        else:
            ret = "0" + ret
        number //= 2
    return ret


def solution(s):
    change_cnt, removed_zero = 0, 0
    while s != "1":
        zero_cnt = s.count("0")
        rest_len = len(s) - zero_cnt
        s = number_to_binary(rest_len)

        change_cnt += 1
        removed_zero += zero_cnt
    return [change_cnt, removed_zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
