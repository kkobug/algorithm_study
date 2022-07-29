"""
https://school.programmers.co.kr/learn/courses/30/lessons/12930
"""
def solution(s):
    answer = ''
    word_idx = 0
    for word in s:
        if word == " ":
            word_idx = 0
            answer += word
            continue

        if word_idx % 2:
            answer += word.lower()
        else:
            answer += word.upper()
        word_idx += 1
    return answer


print(solution("try hello world"))
