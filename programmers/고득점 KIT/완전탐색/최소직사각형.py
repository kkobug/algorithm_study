"""
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""
def solution(sizes):
    max_w = max_h = 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w = w if max_w < w else max_w
        max_h = h if max_h < h else max_h
    answer = max_w * max_h
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
