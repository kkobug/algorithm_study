"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
def solution(phone_book):
    reference = dict()
    for phone_number in phone_book:
        reference[phone_number] = True

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if reference.get(temp) and temp != phone_number:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
