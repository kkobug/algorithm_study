"""
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""
def solution(number, k):
    answer = []
    for n in number:
        while k and answer and answer[-1] < n:
            answer.pop()
            k -= 1

        answer.append(n)
    return ''.join(answer) if not k else ''.join(answer[:-k])


print(solution("1924", 2))
print(solution("11924", 2))
print(solution("111924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
