"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
def solution(brown, yellow):
    width = (brown + 4) // 2 - 3
    height = 3
    while True:
        if (width-2) * (height-2) == yellow:
            return [width, height]
        width -= 1
        height += 1


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
