"""
https://school.programmers.co.kr/learn/courses/30/lessons/12918
"""
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for word in s:
            if not "0" <= word <= "9":
                return False
        return True
    return False


print(solution("a234"))
print(solution("1234"))
