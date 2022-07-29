"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926
"""
def decode(origin, left, right, n):
    origin += n
    if left <= origin <= right:
        return chr(origin)
    else:
        return chr(origin - 26)


def solution(s, n):
    answer = ""
    a_value, z_value, A_value, Z_value = map(ord, "azAZ")

    for word in s:
        if word == " ":
            answer += word
            continue
        word_value = ord(word)
        if a_value <= word_value <= z_value:
            answer += decode(word_value, a_value, z_value, n)
        else:
            answer += decode(word_value, A_value, Z_value, n)
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))



