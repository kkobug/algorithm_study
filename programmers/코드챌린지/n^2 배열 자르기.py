"""
https://programmers.co.kr/learn/courses/30/lessons/87390
"""

def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right)+1):
        share = i // n
        rest = i % n
        answer.append(max(share, rest)+1)
    return answer


print(solution(3, 2, 5))
print()
print(solution(4, 7, 14))
print()
print(solution(1, 0, 0))
print()
print(solution(4, 0, 15))

# solution(10000000, 7, 9235680)
# print(1)
