"""
https://school.programmers.co.kr/learn/courses/30/lessons/64062
"""
def is_crossable(stones, k, number_of_people):
    passed_people = number_of_people
    position = -1
    for p in range(len(stones)):
        stone = stones[p] - passed_people
        if 0 < stone:
            position = p
        else:
            if k <= p - position:
                return False
    return True


def solution(stones, k):
    answer = 1
    max_value = 200000000
    while answer <= max_value:
        mid_value = (answer + max_value) // 2
        crossable = is_crossable(stones, k, mid_value)
        if crossable:
            answer = mid_value + 1
        else:
            max_value = mid_value - 1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
