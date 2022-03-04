"""
https://programmers.co.kr/learn/courses/30/lessons/72410
"""
def solution(new_id):
    answer = ''
    # 1단계
    for id in new_id:
        if ord('A') <= ord(id) <= ord('Z'):
            answer += chr(ord(id) + ord('a') - ord('A'))
        elif ord('a') <= ord(id) <= ord('z'):
            answer += id
        elif ord('0') <= ord(id) <= ord('9'):
            answer += id
        elif id == '-' or id == '_':
            answer += id
        elif id == '.':
            if answer and answer[-1] != '.':
                answer += id
    
    # 4단계
    answer = answer.rstrip('.')

    # 5단계
    if not answer:
        answer = 'a'
    
    # 6단계
    if 15 < len(answer):
        answer = answer[:15].rstrip('.')
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer


new_id_list = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"
]
for new_id in new_id_list:
    print(solution(new_id))