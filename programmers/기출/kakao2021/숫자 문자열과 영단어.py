"""
https://school.programmers.co.kr/learn/courses/30/lessons/81301
"""
def solution(s):
    answer = ""
    idx = 0
    word_to_number = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    temp = ""
    while idx < len(s):
        if "0" <= s[idx] <= "9":
            answer += s[idx]
            idx += 1
        else:
            temp += s[idx]
            if word_to_number.get(temp):
                answer += word_to_number[temp]
                temp = ""
            idx += 1
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
