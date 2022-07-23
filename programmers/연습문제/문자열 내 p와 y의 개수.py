"""
https://school.programmers.co.kr/learn/courses/30/lessons/12916
"""
def solution(s):
    cnt_of_p = cnt_of_y = 0
    for word in s:
        if word == "p" or word == "P":
            cnt_of_p += 1
        elif word == "y" or word == "Y":
            cnt_of_y += 1
    return True if cnt_of_p == cnt_of_y else False


print(solution("pPoooyY"))
print(solution("Pyy"))
