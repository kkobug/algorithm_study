"""
https://school.programmers.co.kr/learn/courses/30/lessons/12917
"""
def solution(s):
    lower = []
    upper = []
    for word in s:
        if "a" <= word <= "z":
            lower.append(word)
        else:
            upper.append(word)
    lower.sort(reverse=True)
    upper.sort(reverse=True)
    return "".join(lower + upper)


print(solution("Zbcdefg"))
