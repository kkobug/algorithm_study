"""
https://school.programmers.co.kr/learn/courses/30/lessons/12903
"""
def solution(s):
    answer = ''
    p = len(s) // 2
    if not len(s) % 2:
        answer += s[p-1]
    answer += s[p]
    return answer


print(solution("abcde"))
print(solution("qwer"))
print(solution("qw"))
